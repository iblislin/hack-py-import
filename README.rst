Hack Your Python Importer
===============================================================================

This repo is a proof of concept to show you python's powerful import system.
Only python 3.6 tested.

We provide following psedo module for you:

- ``pypi``: import anything from the cheese shop

.. code-block:: python

	>>> from pypi import requests
	Collecting requests
	Downloading requests-2.10.0-py2.py3-none-any.whl (506kB)
		100% |████████████████████████████████| 512kB 1.9MB/s
	Installing collected packages: requests
	Successfully installed requests-2.10.0
	>>> requests
	<module 'requests' from '/usr/home/iblis/venv/universe/lib/python3.6/site-packages/requests/__init__.py'>

- ``c``: import c lib via ``cffi`` (maybe work)

.. code-block:: python

    >>> from functools import partial
    >>> from c import stdio
    Requirement already satisfied (use --upgrade to upgrade): cffi in /usr/home/iblis/venv/universe/lib/python3.6/site-packages
    Requirement already satisfied (use --upgrade to upgrade): pycparser in /usr/home/iblis/venv/universe/lib/python3.6/site-packages (from cffi)
    >>> cint = partial(stdio.ffi.cast, 'int')
    >>> stdio.printf(b'Hello PyCon %d!\n', cint(2016))
    Hello PyCon 2016!
    18
