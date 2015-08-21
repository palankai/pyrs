.. pyrs documentation master file, created by
   sphinx-quickstart on Fri Aug 21 08:53:08 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python Microservice framework
=============================

This work is an umbrella package. Itself implements libraries for the packages
which are based on.

Github: `<https://github.com/palankai/pyrs>`_

Sub works
---------

Schema validation, serialization
````````````````````````````````
`<http://pyrs-schema.readthedocs.org/>`_

Restful web framework
`````````````````````

`<http://pyrs-resource.readthedocs.org/>`_

Installation
------------

.. code::

   $ pip install pyrs

Extending the exist functionality
---------------------------------

The `pyrs.ext` and the `pyrs` itself are namespace packages.
If you would like to extend an exist functionality of a package check that
given package documentation for further information.

If you would like to implement a new funcionality, just create a new package
inside `pyrs` package. Make sure the `pyrs` package still remain namespace
package.

Contents
--------

.. toctree::
   :maxdepth: 2

   context



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

