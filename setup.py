#!/usr/bin/env python
#coding=utf-8

from distutils.core import setup
from domainextract import __version__
setup(name='domainextract',
      version=__version__,
      description='extract domain from url or domain',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      py_modules=['domainextract'],
      scripts=['domainextract.py'],
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/domainextract')
