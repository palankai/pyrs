============
Code styling
============

This document would describe how should look like any part of this framework.
I tend to update this document frequently,  specify it as precise as possible.

Language
--------

The language of the comments, documentation, variable names, function names
have to be English. Use syntax and spell checker against any of them.
(It's a bit controversial, because I made lots of spelling mistakes, but I
welcome any improvements.)

PEP8
----

Every python code should be checked with some kind of pep8 checking tool.
Please enable all validation (by default some of the disabled).
None of the PEP8 errors or warning allowed in release version.

The following thumb rules are PEP8 conform.

Use single quote
----------------

Use single quote if it's possible. Double quote only allowed if you can avoid
escaping with it. If you have escaping both ways you should use single quote.

Importing
---------

There should be alphabetically sorted import sections.
The sections are:
 - Future
 - Python Standard Library
 - Third Party
 - Current Python Project
 - Explicitly Local (from . import x)

You should import modules and packages rather than classes or functions if it
could cause a conflict use ``as`` to make an alias. (In some cases importing
a class or a function allowed but try to avoid)

.. code:: python

    from __future__ import absolute_import

    import json
    import os

    import psycopg2
    import werkzeug

    from pyrs.swagger import tests

    from . import base
    from . import conf
