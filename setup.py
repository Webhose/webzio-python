from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='webhoseio',
    packages=['webhoseio'],
    version='0.4',
    author='Ran Geva',
    author_email='ran@webhose.io',
    url='https://github.com/Webhose/webhoseio-python',
    license='MIT',
    description='Simple client library for the webhose.io REST API',
    long_description="",
    install_requires=[
        "requests >= 2.0.0"
    ],
    classifiers=(
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
    )
)
