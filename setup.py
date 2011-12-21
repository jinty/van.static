##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os
from setuptools import setup, find_packages

setup(name="van.static",
      version='0.1',
      license='BSD-derived',
      url='http://pypi.python.org/pypi/van.static',
      author_email='brian@vanguardistas.net',
      packages=find_packages(),
      author="Vanguardistas LLC",
      description="Tools for managing Pyramid static files on a CDN",
      test_suite="van.static.tests",
      namespace_packages=["van"],
      install_requires = [
          'setuptools',
          ],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Development Status :: 3 - Alpha',
          'Framework :: Pylons', # actually pyramid, but that's part of pylons
          ],
      include_package_data = True,
      )
