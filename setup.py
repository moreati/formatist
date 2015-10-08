from setuptools import setup

import io
import os


def read(fname):
    here = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(here, fname), encoding='utf-8') as f:
        return f.read()


setup(
    name='formatist',
    version='0.0.2',

    description='Converts %-style format strings to newer {}-style',
    long_description=read('README.rst'),

    url='https://github.com/moreati/formatist',
    author='Glyph',
    author_email='glyph@twistedmatrix.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='string format pep3101 percent braces',

    py_modules=[
        'formatist',
    ],
)

