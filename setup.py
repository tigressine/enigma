#! /usr/bin/env python3
from setuptools import setup

def load_description():
    try:
        with open('docs/README.md', 'r') as f:
            long_description = f.read()
    except FileNotFoundError:
        long_description = 'something'###
    return long_description

setup(
    name='Enigma',
    version='1.0.0',
    author='Tiger Sachse',
    description='Protect your correspondence from Allied spies!',
    long_description=load_description(),
    url='https://github.com/tgsachse/enigma',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Environment :: COnsole',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications',
        'Topic :: Security :: Cryptography',
        'Topic :: Text Processing'],
    keywords='enigma encryption wwii cryptography hidden messages germany war',
    packages=['enigma'],
    python_requires='>=3',
    data_files=[
        ('bin', ['enigma/enigma']),
        ('share/doc/enigma', ['docs/LICENSE.txt', 'docs/README.md']),
        ('share/enigma', ['enigma/data/daily_sheet.db'])]
    )
