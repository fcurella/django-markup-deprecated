import os
from setuptools import setup, find_packages

from markup_deprecated import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = []

setup(
    name = "Django Markup Deprecated",
    version = ".".join(map(str, __version__)),
    description = "Original django.contrib.markup from Django 1.4.1.",
    long_description = read('README.rst'),
    url = 'https://github.com/fcurella/django-markup-deprecated',
    license = 'BSD',
    mainteiner = 'Flavio Curella',
    mainteiner_email = 'flavio.curella@gmail.com',
    packages = find_packages(exclude=['tests']),
    include_package_data = True,
    classifiers = [
        'Development Status :: 7 - Inactive',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
