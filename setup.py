#!/usr/bin/env python3
"""Setup script for CryptXT"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="cryptxt",
    version="1.0.1",
    author="vyofgod",
    description="Military-grade file and message encryption tool with AES-256-GCM and Argon2id",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vyofgod/CryptXT",
    project_urls={
        "Bug Reports": "https://github.com/vyofgod/CryptXT/issues",
        "Source": "https://github.com/vyofgod/CryptXT",
        "Documentation": "https://github.com/vyofgod/CryptXT#readme",
    },
    packages=find_packages(),
    py_modules=["cryptxt"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Console",
    ],
    keywords="encryption, security, cryptography, aes-256, argon2, cli, terminal, privacy, file-encryption",
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=41.0.0",
        "argon2-cffi>=23.1.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "cryptxt=cryptxt:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
