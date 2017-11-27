#! /usr/bin/env python3
from setuptools import setup

def load_description():
    with open('docs/README.md', 'r') as f:
        long_description = f.read()
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
        'Environment :: Console',
        'Topic :: Communications',
        'Topic :: Text Processing',
        'Natural Language :: English',
        'Development Status :: 5 - Stable',
        'Topic :: Security :: Cryptography',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
    keywords='enigma encryption wwii cryptography hidden messages germany war',
    packages=['enigmamachine'],
    python_requires='>=3',
    data_files=[
        ('bin', ['enigmamachine/enigma']),
        ('share/man/man1', ['docs/enigma.1']),
        ('share/enigma', ['enigmamachine/data/enigma.db']),
        ('share/doc/enigma', ['docs/LICENSE.txt', 'docs/README.md'])]
    )
