#!/usr/bin/env python
#coding=utf-8

from distutils.core import setup
from pydnspodint import __version__
setup(name='pydnspodint',
      version=__version__,
      description='A dnspod international version sdk',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      packages=['pydnspodint'],
      package_dir={'pydnspodint': 'pydnspodint'},
      package_data={'pydnspodint': ['stuff']},
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/pydnspodint')
