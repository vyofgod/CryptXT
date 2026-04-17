#!/usr/bin/env node

const { spawn } = require('child_process');

console.log('CryptXT - Post-install setup');
console.log('');

// Check Python
function checkPython() {
    return new Promise((resolve) => {
        const python = process.platform === 'win32' ? 'python' : 'python3';
        const check = spawn(python, ['--version']);
        
        check.on('close', (code) => {
            if (code === 0) {
                console.log('✓ Python found');
                resolve(python);
            } else {
                resolve(null);
            }
        });
        
        check.on('error', () => {
            resolve(null);
        });
    });
}

// Install dependencies
async function install() {
    const python = await checkPython();
    
    if (!python) {
        console.log('⚠ Python 3.7+ not found');
        console.log('Please install Python from: https://www.python.org/downloads/');
        console.log('');
        console.log('After installing Python, run:');
        console.log('  pip3 install cryptography argon2-cffi rich');
        return;
    }
    
    console.log('Installing Python dependencies...');
    const pip = process.platform === 'win32' ? 'pip' : 'pip3';
    
    const install = spawn(pip, ['install', 'cryptography', 'argon2-cffi', 'rich'], {
        stdio: 'inherit'
    });
    
    install.on('close', (code) => {
        if (code === 0) {
            console.log('');
            console.log('✓ Installation complete!');
            console.log('');
            console.log('Run CryptXT with:');
            console.log('  npx cryptxt');
            console.log('or');
            console.log('  cryptxt  (if installed globally)');
        } else {
            console.log('');
            console.log('⚠ Failed to install dependencies');
            console.log('Please install manually:');
            console.log('  pip3 install cryptography argon2-cffi rich');
        }
    });
}

install();
