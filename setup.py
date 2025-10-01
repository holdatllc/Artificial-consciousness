#!/usr/bin/env python3
"""
Setup script for HCM (Human Consciousness Modeling) System
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="hcm-system",
    version="1.0.0",
    author="MHM Research Team",
    author_email="research@mhm-systems.com",
    description="Human Consciousness Modeling system for integrating real brain patterns into computational systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mhm-research/hcm-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="consciousness modeling, computational optimization, cryptocurrency mining, nuclear physics, AI enhancement",
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0",
        "pyyaml>=5.4.0",
        "psutil>=5.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "gpu": [
            "torch>=1.9.0",
            "tensorflow>=2.6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "hcm-validate=tests.hcm_validation_test:main",
            "hcm-demo=examples.test_hcm_standalone:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="consciousness modeling, EEG, brain patterns, AI enhancement, neural processing",
    project_urls={
        "Bug Reports": "https://github.com/mhm-research/hcm-system/issues",
        "Source": "https://github.com/mhm-research/hcm-system",
        "Documentation": "https://hcm-system.readthedocs.io/",
        "Funding": "https://github.com/sponsors/mhm-research",
    },
)
