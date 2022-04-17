from codecs import open
from pathlib import Path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("pypi-desc", 'r') as _readme_file:
    long_description = _readme_file.read()

setup(
    name='webzio',
    packages=['webzio'],
    version='1.0.1',
    author='Ran Geva',
    author_email='ran@webz.io',
    url='https://github.com/webhose/webzio-python',
    license='MIT',
    description='Simple client library for the webz.io REST API',
    long_description=long_description,
    install_requires=[
        "requests >= 2.0.0"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
