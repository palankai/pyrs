#!/usr/bin/env python

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyrs',
    author='Csaba Palankai',
    author_email='csaba.palankai@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    version='0.3.2',
    description="Python microservice framework",
    url='http://pyrs.readthedocs.org/',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved ::'
            ' GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=('service', 'rest', 'restful', 'swagger', 'resource'),
    zip_safe=False,
#    namespace_packages = ['pyrs'],
    install_requires=[r for r in read("requirements.txt").split("\n") if r],
)
