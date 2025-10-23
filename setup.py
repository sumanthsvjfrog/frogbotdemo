#!/usr/bin/env python

from setuptools import setup

setup(
    name='jfrog-python-example',
    version='1.0',
    description='Project example for building Python project with JFrog products',
    author='JFrog',
    author_email='jfrog@jfrog.com',
    url='https://github.com/jfrog/project-examples',
    packages=['pythonExample'],
    install_requires=['nltk', 'Django==2.2.0', 'requests==2.18.0'],
)
