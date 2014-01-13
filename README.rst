Django Markup Deprecated
======================================

This package contains the original ``django.contrib.markup`` from Django 1.4.1.

It's intended as backward-compatible quick fix for your project if you're upgrading to
Django 1.6, which deprecates the app.

For new projects, you may want to use something like `Django Markup Field <https://github.com/jamesturk/django-markupfield>`_ instead.

Installation
------------

This package is also available on PyPI.
::

    $ pip install django-markup-deprecated

Usage
-----

Add ``'markup_deprecated'`` to your ``INSTALLED_APPS``.

The template library is still called ``markup``, so you can still use ``{% load markup %}`` in your templates.

Difference from ``django.contrib.markup``
-----------------------------------------

Settings
~~~~~~~~
This package adds an optional ``DJANGO_MARKUP_IGNORE_WARNINGS`` setting, that can be used to silence the warnings. Defaults to ``False``.

Support
-------

This package will updated only when (and if) ``django.contrib.markup`` will ever
change in the Django 1.4.x series. It is only for backward-compatibility purposes
and there will be no support nor bugfixes.
