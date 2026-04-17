#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CryptXT - Advanced File and Message Encryption Tool
Enhanced security with AES-256-GCM, Argon2id, and HMAC verification

Required packages:
pip install cryptography argon2-cffi rich
"""

import os
import sys
import hmac
import hashlib
import secrets
from pathlib import Path
from typing import Optional, Tuple

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
try:
    from argon2 import PasswordHasher
    from argon2.low_level import hash_secret_raw, Type
    ARGON2_AVAILABLE = True
except ImportError:
    ARGON2_AVAILABLE = False

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.text import Text
from rich import box
from rich.align import Align
import time

console = Console()


class CryptXT:
    """
    Advanced encryption manager with multiple security layers:
    - AES-256-GCM (Authenticated Encryption)
    - Argon2id key derivation (memory-hard, resistant to GPU attacks)
    - HMAC-SHA256 integrity verification
    - Secure random salt generation
    """
    
    VERSION = "1.0.1"
    SALT_SIZE = 32
    NONCE_SIZE = 12  # GCM standard nonce size
    TAG_SIZE = 16    # GCM authentication tag size
    
    # Argon2id parameters (OWASP recommendations 2024)
    ARGON2_TIME_COST = 3        # iterations
    ARGON2_MEMORY_COST = 65536  # 64 MB
    ARGON2_PARALLELISM = 4      # threads
    
    # PBKDF2 fallback parameters
    PBKDF2_ITERATIONS = 600000  # OWASP 2024 recommendation
    
    def __init__(self):
        self.use_argon2 = ARGON2_AVAILABLE
        if not self.use_argon2:
            console.print("[yellow]WARNING: Argon2 not available, using PBKDF2 (less secure)[/yellow]")
            console.print("[dim]Install argon2-cffi for enhanced security: pip install argon2-cffi[/dim]\n")
    
    def derive_key_argon2(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key using Argon2id (recommended)"""
        key = hash_secret_raw(
            secret=password.encode(),
            salt=salt,
            time_cost=self.ARGON2_TIME_COST,
            memory_cost=self.ARGON2_MEMORY_COST,
            parallelism=self.ARGON2_PARALLELISM,
            hash_len=32,
            type=Type.ID  # Argon2id - hybrid mode
        )
        return key
    
    def derive_key_pbkdf2(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key using PBKDF2 (fallback)"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=self.PBKDF2_ITERATIONS,
        )
        return kdf.derive(password.encode())
    
    def derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key using best available method"""
        if self.use_argon2:
            return self.derive_key_argon2(password, salt)
        else:
            return self.derive_key_pbkdf2(password, salt)
    
    def generate_hmac(self, key: bytes, data: bytes) -> bytes:
        """Generate HMAC-SHA256 for integrity verification"""
        return hmac.new(key, data, hashlib.sha256).digest()
    
    def verify_hmac(self, key: bytes, data: bytes, expected_hmac: bytes) -> bool:
        """Verify HMAC-SHA256"""
        return hmac.compare_digest(self.generate_hmac(key, data), expected_hmac)
    
    def encrypt_data(self, data: bytes, password: str) -> bytes:
        """
        Encrypt data with AES-256-GCM
        
        Format: SALT(32) + NONCE(12) + HMAC(32) + CIPHERTEXT+TAG
        """
        # Generate random salt and nonce
        salt = secrets.token_bytes(self.SALT_SIZE)
        nonce = secrets.token_bytes(self.NONCE_SIZE)
        
        # Derive encryption key
        key = self.derive_key(password, salt)
        
        # Encrypt with AES-256-GCM (includes authentication tag)
        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, data, None)
        
        # Generate HMAC for additional integrity check
        hmac_key = hashlib.sha256(key + b"hmac").digest()
        data_to_hmac = salt + nonce + ciphertext
        hmac_value = self.generate_hmac(hmac_key, data_to_hmac)
        
        # Combine all components
        encrypted_data = salt + nonce + hmac_value + ciphertext
        return encrypted_data
    
    def decrypt_data(self, encrypted_data: bytes, password: str) -> Tuple[bool, bytes]:
        """
        Decrypt data with AES-256-GCM
        
        Returns: (success, decrypted_data or error_message)
        """
        try:
            # Extract components
            if len(encrypted_data) < self.SALT_SIZE + self.NONCE_SIZE + 32 + self.TAG_SIZE:
                return False, b"Invalid encrypted data format"
            
            salt = encrypted_data[:self.SALT_SIZE]
            nonce = encrypted_data[self.SALT_SIZE:self.SALT_SIZE + self.NONCE_SIZE]
            hmac_value = encrypted_data[self.SALT_SIZE + self.NONCE_SIZE:self.SALT_SIZE + self.NONCE_SIZE + 32]
            ciphertext = encrypted_data[self.SALT_SIZE + self.NONCE_SIZE + 32:]
            
            # Derive key
            key = self.derive_key(password, salt)
            
            # Verify HMAC
            hmac_key = hashlib.sha256(key + b"hmac").digest()
            data_to_verify = salt + nonce + ciphertext
            if not self.verify_hmac(hmac_key, data_to_verify, hmac_value):
                return False, b"HMAC verification failed - data may be corrupted or tampered"
            
            # Decrypt with AES-256-GCM
            aesgcm = AESGCM(key)
            plaintext = aesgcm.decrypt(nonce, ciphertext, None)
            
            return True, plaintext
            
        except Exception as e:
            return False, f"Decryption failed: {str(e)}".encode()
    
    def encrypt_message(self, message: str, password: str) -> str:
        """Encrypt message and return base64 encoded string"""
        import base64
        encrypted = self.encrypt_data(message.encode('utf-8'), password)
        return base64.b64encode(encrypted).decode('ascii')
    
    def decrypt_message(self, encrypted_message: str, password: str) -> Tuple[bool, str]:
        """Decrypt base64 encoded message"""
        import base64
        try:
            encrypted_data = base64.b64decode(encrypted_message.encode('ascii'))
            success, result = self.decrypt_data(encrypted_data, password)
            if success:
                return True, result.decode('utf-8')
            else:
                return False, result.decode('utf-8')
        except Exception as e:
            return False, f"Decryption error: {str(e)}"
    
    def encrypt_file(self, file_path: str, password: str) -> Tuple[bool, str]:
        """Encrypt file and save with .cryptxt extension"""
        try:
            path = Path(file_path)
            if not path.exists():
                return False, "File not found"
            
            if not path.is_file():
                return False, "Not a file"
            
            # Read file
            with open(path, 'rb') as f:
                file_data = f.read()
            
            # Encrypt
            encrypted_data = self.encrypt_data(file_data, password)
            
            # Save with .cryptxt extension
            encrypted_path = path.with_suffix(path.suffix + '.cryptxt')
            with open(encrypted_path, 'wb') as f:
                f.write(encrypted_data)
            
            return True, str(encrypted_path)
            
        except PermissionError:
            return False, "Permission denied"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def decrypt_file(self, file_path: str, password: str) -> Tuple[bool, str]:
        """Decrypt .cryptxt file and restore original"""
        try:
            path = Path(file_path)
            if not path.exists():
                return False, "File not found"
            
            if not str(path).endswith('.cryptxt'):
                return False, "Not a .cryptxt file"
            
            # Read encrypted file
            with open(path, 'rb') as f:
                encrypted_data = f.read()
            
            # Decrypt
            success, result = self.decrypt_data(encrypted_data, password)
            if not success:
                return False, result.decode('utf-8')
            
            # Restore original file
            original_path = path.with_suffix('')
            with open(original_path, 'wb') as f:
                f.write(result)
            
            return True, str(original_path)
            
        except PermissionError:
            return False, "Permission denied"
        except Exception as e:
            return False, f"Error: {str(e)}"


class CryptXTUI:
    """Terminal User Interface for CryptXT"""
    
    def __init__(self):
        self.crypto = CryptXT()
    
    def show_banner(self):
        """Display application banner"""
        banner = """
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗  ██╗████████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝╚██╗██╔╝╚══██╔══╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║    ╚███╔╝    ██║   
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║    ██╔██╗    ██║   
╚██████╗██║  ██║   ██║   ██║        ██║   ██╔╝ ██╗   ██║   
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝  ╚═╝   ╚═╝   
        """
        
        title = Text(banner, style="bold cyan")
        subtitle = Text("Advanced File & Message Encryption", style="bold yellow")
        
        kdf_method = "Argon2id" if self.crypto.use_argon2 else "PBKDF2"
        info = Text(f"AES-256-GCM + {kdf_method} + HMAC | v{CryptXT.VERSION}", style="dim")
        
        console.print()
        console.print(Align.center(title))
        console.print(Align.center(subtitle))
        console.print(Align.center(info))
        console.print()
    
    def show_menu(self) -> str:
        """Display main menu"""
        table = Table(
            title="Main Menu",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
            border_style="cyan"
        )
        
        table.add_column("Option", style="cyan", justify="center", width=10)
        table.add_column("Action", style="yellow", width=40)
        
        table.add_row("1", "Encrypt Message")
        table.add_row("2", "Decrypt Message")
        table.add_row("3", "Encrypt File")
        table.add_row("4", "Decrypt File")
        table.add_row("5", "Security Info")
        table.add_row("6", "Exit")
        
        console.print(table)
        console.print()
        
        choice = Prompt.ask(
            "[bold cyan]Your choice[/bold cyan]",
            choices=["1", "2", "3", "4", "5", "6"],
            default="1"
        )
        return choice
    
    def show_security_info(self):
        """Display security information"""
        kdf_method = "Argon2id" if self.crypto.use_argon2 else "PBKDF2"
        
        if self.crypto.use_argon2:
            kdf_details = f"""
[green]OK[/green] Argon2id (Winner of Password Hashing Competition)
  - Time cost: {CryptXT.ARGON2_TIME_COST} iterations
  - Memory cost: {CryptXT.ARGON2_MEMORY_COST} KB ({CryptXT.ARGON2_MEMORY_COST // 1024} MB)
  - Parallelism: {CryptXT.ARGON2_PARALLELISM} threads
  - Resistant to GPU/ASIC attacks
            """
        else:
            kdf_details = f"""
[yellow]WARNING[/yellow] PBKDF2-HMAC-SHA256 (Fallback)
  - Iterations: {CryptXT.PBKDF2_ITERATIONS:,}
  - [dim]Install argon2-cffi for better security[/dim]
            """
        
        info = f"""
[bold cyan]Encryption Algorithm:[/bold cyan]
[green]OK[/green] AES-256-GCM (Authenticated Encryption)
  - 256-bit key length
  - Galois/Counter Mode with authentication
  - Built-in integrity verification

[bold cyan]Key Derivation Function:[/bold cyan]{kdf_details}

[bold cyan]Additional Security:[/bold cyan]
[green]OK[/green] HMAC-SHA256 integrity verification
[green]OK[/green] Cryptographically secure random salt ({CryptXT.SALT_SIZE} bytes)
[green]OK[/green] Unique nonce per encryption ({CryptXT.NONCE_SIZE} bytes)
[green]OK[/green] Authentication tag prevents tampering ({CryptXT.TAG_SIZE} bytes)

[bold cyan]Security Level:[/bold cyan]
[green]Military-grade encryption[/green] - Suitable for highly sensitive data
        """
        
        console.print(Panel(
            info,
            title="Security Information",
            border_style="green",
            padding=(1, 2)
        ))
        console.print()
    
    def encrypt_message_ui(self):
        """Message encryption interface"""
        console.print(Panel.fit(
            "[bold yellow]Encrypt Message[/bold yellow]",
            border_style="cyan"
        ))
        console.print()
        
        message = Prompt.ask("[cyan]Message to encrypt[/cyan]")
        if not message:
            console.print("[red]ERROR: Message cannot be empty[/red]")
            return
        
        password = Prompt.ask("[cyan]Master password[/cyan]", password=True)
        if not password:
            console.print("[red]ERROR: Password cannot be empty[/red]")
            return
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Encrypting...", total=100)
            
            for i in range(100):
                time.sleep(0.008)
                progress.update(task, advance=1)
            
            encrypted = self.crypto.encrypt_message(message, password)
        
        console.print()
        console.print(Panel(
            f"[green]SUCCESS: Message encrypted successfully[/green]\n\n"
            f"[yellow]Encrypted message:[/yellow]\n[dim]{encrypted}[/dim]",
            title="Result",
            border_style="green"
        ))
        console.print()
    
    def decrypt_message_ui(self):
        """Message decryption interface"""
        console.print(Panel.fit(
            "[bold yellow]Decrypt Message[/bold yellow]",
            border_style="cyan"
        ))
        console.print()
        
        encrypted_message = Prompt.ask("[cyan]Encrypted message (Base64)[/cyan]")
        if not encrypted_message:
            console.print("[red]ERROR: Message cannot be empty[/red]")
            return
        
        password = Prompt.ask("[cyan]Master password[/cyan]", password=True)
        if not password:
            console.print("[red]ERROR: Password cannot be empty[/red]")
            return
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Decrypting...", total=100)
            
            for i in range(100):
                time.sleep(0.008)
                progress.update(task, advance=1)
            
            success, result = self.crypto.decrypt_message(encrypted_message, password)
        
        console.print()
        if success:
            console.print(Panel(
                f"[green]SUCCESS: Message decrypted successfully[/green]\n\n"
                f"[yellow]Original message:[/yellow]\n{result}",
                title="Result",
                border_style="green"
            ))
        else:
            console.print(Panel(
                f"[red]ERROR: {result}[/red]",
                title="Error",
                border_style="red"
            ))
        console.print()
    
    def encrypt_file_ui(self):
        """File encryption interface"""
        console.print(Panel.fit(
            "[bold yellow]Encrypt File[/bold yellow]",
            border_style="cyan"
        ))
        console.print()
        
        file_path = Prompt.ask("[cyan]File path[/cyan]")
        if not file_path:
            console.print("[red]ERROR: File path cannot be empty[/red]")
            return
        
        password = Prompt.ask("[cyan]Master password[/cyan]", password=True)
        if not password:
            console.print("[red]ERROR: Password cannot be empty[/red]")
            return
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Encrypting file...", total=100)
            
            for i in range(100):
                time.sleep(0.015)
                progress.update(task, advance=1)
            
            success, result = self.crypto.encrypt_file(file_path, password)
        
        console.print()
        if success:
            console.print(Panel(
                f"[green]SUCCESS: File encrypted successfully[/green]\n\n"
                f"[yellow]Encrypted file:[/yellow]\n{result}",
                title="Result",
                border_style="green"
            ))
        else:
            console.print(Panel(
                f"[red]ERROR: {result}[/red]",
                title="Error",
                border_style="red"
            ))
        console.print()
    
    def decrypt_file_ui(self):
        """File decryption interface"""
        console.print(Panel.fit(
            "[bold yellow]Decrypt File[/bold yellow]",
            border_style="cyan"
        ))
        console.print()
        
        file_path = Prompt.ask("[cyan]Encrypted file path (.cryptxt)[/cyan]")
        if not file_path:
            console.print("[red]ERROR: File path cannot be empty[/red]")
            return
        
        password = Prompt.ask("[cyan]Master password[/cyan]", password=True)
        if not password:
            console.print("[red]ERROR: Password cannot be empty[/red]")
            return
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Decrypting file...", total=100)
            
            for i in range(100):
                time.sleep(0.015)
                progress.update(task, advance=1)
            
            success, result = self.crypto.decrypt_file(file_path, password)
        
        console.print()
        if success:
            console.print(Panel(
                f"[green]SUCCESS: File decrypted successfully[/green]\n\n"
                f"[yellow]Original file:[/yellow]\n{result}",
                title="Result",
                border_style="green"
            ))
        else:
            console.print(Panel(
                f"[red]ERROR: {result}[/red]",
                title="Error",
                border_style="red"
            ))
        console.print()
    
    def run(self):
        """Main application loop"""
        try:
            self.show_banner()
            
            while True:
                choice = self.show_menu()
                console.print()
                
                if choice == "1":
                    self.encrypt_message_ui()
                elif choice == "2":
                    self.decrypt_message_ui()
                elif choice == "3":
                    self.encrypt_file_ui()
                elif choice == "4":
                    self.decrypt_file_ui()
                elif choice == "5":
                    self.show_security_info()
                elif choice == "6":
                    console.print(Panel(
                        "[bold yellow]Stay secure![/bold yellow]",
                        border_style="cyan"
                    ))
                    break
                
                console.print("[dim]Press Enter to continue...[/dim]")
                input()
                console.clear()
                self.show_banner()
        
        except KeyboardInterrupt:
            console.print("\n\n[yellow]WARNING: Application terminated by user[/yellow]")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[red]ERROR: Unexpected error: {str(e)}[/red]")
            sys.exit(1)


def main():
    """Application entry point"""
    app = CryptXTUI()
    app.run()


if __name__ == "__main__":
    main()
