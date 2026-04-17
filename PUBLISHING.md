# Publishing CryptXT to PyPI and npm

Complete guide to publish CryptXT as both a pip and npm package.

---

## Publishing to PyPI (pip)

### Prerequisites

1. **Create PyPI account**: https://pypi.org/account/register/
2. **Install build tools**:
   ```bash
   pip install --upgrade build twine
   ```

### Step 1: Build the Package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python3 -m build
```

This creates:
- `dist/cryptxt-1.0.0.tar.gz` (source distribution)
- `dist/cryptxt-1.0.0-py3-none-any.whl` (wheel distribution)

### Step 2: Test on TestPyPI (Optional but Recommended)

```bash
# Upload to TestPyPI
python3 -m twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ cryptxt

# Test the command
cryptxt
```

### Step 3: Upload to PyPI

```bash
# Upload to PyPI
python3 -m twine upload dist/*

# Enter your PyPI username and password when prompted
```

### Step 4: Verify Installation

```bash
# Install from PyPI
pip install cryptxt

# Run the application
cryptxt
```

### Users Can Now Install With:

```bash
# Install
pip install cryptxt

# Run
cryptxt
```

Or use directly with pipx:

```bash
# Install pipx
pip install pipx

# Run CryptXT without installing
pipx run cryptxt
```

---

## Publishing to npm (npx)

### Prerequisites

1. **Create npm account**: https://www.npmjs.com/signup
2. **Install Node.js**: https://nodejs.org/
3. **Login to npm**:
   ```bash
   npm login
   ```

### Step 1: Test Locally

```bash
# Test the package locally
npm link

# Run it
cryptxt

# Or test with npx
npx .
```

### Step 2: Publish to npm

```bash
# Make sure you're in the project directory
cd CryptXT

# Publish
npm publish
```

If the name is taken, you can publish with a scope:

```bash
# Update package.json name to "@yourusername/cryptxt"
npm publish --access public
```

### Step 3: Verify Installation

```bash
# Test with npx (no installation needed)
npx cryptxt

# Or install globally
npm install -g cryptxt

# Run
cryptxt
```

### Users Can Now Use With:

```bash
# Run directly with npx (no installation)
npx cryptxt

# Or install globally
npm install -g cryptxt
cryptxt

# Or install locally
npm install cryptxt
npx cryptxt
```

---

## Version Updates

### Update Version Number

1. **Update version in all files**:
   - `pyproject.toml` → version = "1.0.1"
   - `setup.py` → version="1.0.1"
   - `package.json` → "version": "1.0.1"
   - `cryptxt.py` → VERSION = "1.0.1"

2. **Commit changes**:
   ```bash
   git add .
   git commit -m "Bump version to 1.0.1"
   git tag v1.0.1
   git push origin main --tags
   ```

### Publish Updates

**PyPI:**
```bash
rm -rf build/ dist/ *.egg-info/
python3 -m build
python3 -m twine upload dist/*
```

**npm:**
```bash
npm publish
```

---

## Installation Methods Summary

### For End Users

#### Method 1: pip (Python Package)
```bash
pip install cryptxt
cryptxt
```

#### Method 2: pipx (Isolated Python Environment)
```bash
pipx install cryptxt
cryptxt
```

#### Method 3: npx (No Installation)
```bash
npx cryptxt
```

#### Method 4: npm Global Install
```bash
npm install -g cryptxt
cryptxt
```

#### Method 5: Git Clone (Development)
```bash
git clone https://github.com/vyofgod/CryptXT.git
cd CryptXT
pip install -r requirements.txt
python3 cryptxt.py
```

---

## Package URLs

After publishing, your package will be available at:

- **PyPI**: https://pypi.org/project/cryptxt/
- **npm**: https://www.npmjs.com/package/cryptxt
- **GitHub**: https://github.com/vyofgod/CryptXT

---

## Troubleshooting

### PyPI Upload Issues

**Error: "Package already exists"**
- You cannot re-upload the same version
- Increment version number and rebuild

**Error: "Invalid credentials"**
- Use API token instead of password
- Generate token at: https://pypi.org/manage/account/token/
- Username: `__token__`
- Password: `pypi-...` (your token)

### npm Publish Issues

**Error: "Package name taken"**
- Use scoped package: `@yourusername/cryptxt`
- Update package.json name
- Publish with: `npm publish --access public`

**Error: "Need to login"**
```bash
npm login
npm whoami  # Verify login
```

---

## Best Practices

1. **Test before publishing**:
   - Test on TestPyPI first
   - Test with `npm link` locally
   - Verify all dependencies work

2. **Version management**:
   - Follow semantic versioning (MAJOR.MINOR.PATCH)
   - Update CHANGELOG.md
   - Create git tags for releases

3. **Documentation**:
   - Keep README.md updated
   - Include installation instructions
   - Add usage examples

4. **Security**:
   - Never commit API tokens
   - Use `.npmrc` and `.pypirc` for credentials
   - Enable 2FA on PyPI and npm accounts

---

## Quick Publish Commands

### First Time Publish

```bash
# PyPI
python3 -m build
python3 -m twine upload dist/*

# npm
npm publish
```

### Update and Republish

```bash
# Update version in files
# Then:

# PyPI
rm -rf build/ dist/ *.egg-info/
python3 -m build
python3 -m twine upload dist/*

# npm
npm publish

# Git
git add .
git commit -m "Release v1.0.1"
git tag v1.0.1
git push origin main --tags
```

---

## Support

- **PyPI Package**: https://pypi.org/project/cryptxt/
- **npm Package**: https://www.npmjs.com/package/cryptxt
- **GitHub Issues**: https://github.com/vyofgod/CryptXT/issues
- **Documentation**: https://github.com/vyofgod/CryptXT#readme
