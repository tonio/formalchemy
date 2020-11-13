# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import xml.sax.saxutils
from os.path import join
import sys
import os

def get_version(fname='formalchemy/__init__.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])

def read(filename):
    text = open(filename,'r').read()
    return xml.sax.saxutils.escape(text)

long_description = '.. contents:: :depth: 1\n\n' +\
                   'Description\n' +\
                   '===========\n\n' +\
                   read('README.txt') +\
                   '\n\n' +\
                   read('CHANGELOG.rst')

setup(name='FormAlchemy',
      license='MIT License',
      version=get_version(),
      description='FormAlchemy greatly speeds development with SQLAlchemy mapped classes (models) in a HTML forms environment.',
      long_description=long_description,
      author='Alexandre Conrad, Jonathan Ellis, Gaël Pasgrimaud, Matthias Urlichs',
      author_email='formalchemy@googlegroups.com',
      url='https://github.com/FormAlchemy/formalchemy',
      install_requires=['SQLAlchemy', 'Tempita', 'WebHelpers2', 'WebOb', 'MarkupSafe', 'six'],
      packages=find_packages(exclude=('formalchemy.tests',)),
      package_data={'formalchemy': ['*.tmpl', 'i18n_resources/*/LC_MESSAGES/formalchemy.mo',
                                    'ext/pylons/*.mako', 'ext/pylons/resources/*.css', 'ext/pylons/resources/*.png',
                                    'tests/data/mako/*.mako', 'tests/data/genshi/*.html',
                                    'paster_templates/pylons_fa/+package+/*/*_tmpl',
                                    ]},
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Text Processing :: Markup :: HTML',
          'Topic :: Utilities',
      ],
      message_extractors = {'formalchemy': [
              ('**.py', 'python', None),
              ('**.mako', 'mako', None),
              ('**.tmpl', 'python', None)]},
      zip_safe=False,
      entry_points = """
      [paste.paster_create_template]
      pylons_fa = formalchemy.ext.pylons.pastertemplate:PylonsTemplate
      """,
      )

