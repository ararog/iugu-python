"""A python API for IUGU.

See:
https://github.com/ararog/iugu-python
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")

    def read_md(f):
        return open(f, 'r').read()

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version('iugu')

setup(
    name='iugu',
    version=version,
    description='A python API for IUGU',
    long_description=read_md('README.md'),
    url='https://github.com/ararog/iugu-python',
    author='Rogerio Pereira Araujo',
    author_email='rogerio.araujo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='sample setuptools development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['peppercorn'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    }
)
