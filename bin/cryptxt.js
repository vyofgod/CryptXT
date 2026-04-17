#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

// Check if Python is installed
function checkPython() {
    return new Promise((resolve) => {
        const python = process.platform === 'win32' ? 'python' : 'python3';
        const check = spawn(python, ['--version']);
        
        check.on('close', (code) => {
            resolve(code === 0 ? python : null);
        });
        
        check.on('error', () => {
            resolve(null);
        });
    });
}

// Install Python dependencies
function installDependencies(python) {
    return new Promise((resolve, reject) => {
        console.log('Installing Python dependencies...');
        const pip = process.platform === 'win32' ? 'pip' : 'pip3';
        const install = spawn(pip, ['install', 'cryptography', 'argon2-cffi', 'rich'], {
            stdio: 'inherit'
        });
        
        install.on('close', (code) => {
            if (code === 0) {
                resolve();
            } else {
                reject(new Error('Failed to install dependencies'));
            }
        });
    });
}

// Run CryptXT
async function runCryptXT() {
    const python = await checkPython();
    
    if (!python) {
        console.error('ERROR: Python 3.7+ is required but not found.');
        console.error('Please install Python from: https://www.python.org/downloads/');
        process.exit(1);
    }
    
    const scriptPath = path.join(__dirname, '..', 'cryptxt.py');
    
    if (!fs.existsSync(scriptPath)) {
        console.error('ERROR: cryptxt.py not found');
        process.exit(1);
    }
    
    // Check if dependencies are installed
    const checkDeps = spawn(python, ['-c', 'import cryptography, argon2, rich']);
    
    checkDeps.on('close', async (code) => {
        if (code !== 0) {
            console.log('Python dependencies not found. Installing...');
            try {
                await installDependencies(python);
            } catch (error) {
                console.error('Failed to install dependencies. Please run manually:');
                console.error('  pip3 install cryptography argon2-cffi rich');
                process.exit(1);
            }
        }
        
        // Run the Python script
        const cryptxt = spawn(python, [scriptPath], {
            stdio: 'inherit'
        });
        
        cryptxt.on('close', (code) => {
            process.exit(code);
        });
    });
}

runCryptXT();
