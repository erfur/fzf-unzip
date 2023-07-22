#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ['Click>=7.0', 'krfzf-py>=0.0.4']

test_requirements = [ ]

setup(
    author="Furkan Er",
    author_email='erfur@mailbox.org',
    python_requires='>=3.6',
    description="Use fzf to select which files to unzip",
    entry_points={
        'console_scripts': [
            'fzf_unzip=fzf_unzip.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    name='fzf_unzip',
    packages=find_packages(include=['fzf_unzip', 'fzf_unzip.*']),
    url='https://github.com/erfur/fzf_unzip',
    version='0.1.0',
    zip_safe=False,
)
