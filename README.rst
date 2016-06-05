Hack Your Python Importer
===============================================================================

This repo is a proof of concept to show you python's powerful import system.
Only python 3.6 tested.

We provide following psedo module for you:

- ``pypi``
- ``c``


``pypi``: import anything from the cheese shop
----------------------------------------------------------------------

.. code-block:: python

	>>> from pypi import requests
	Collecting requests
	Downloading requests-2.10.0-py2.py3-none-any.whl (506kB)
		100% |████████████████████████████████| 512kB 1.9MB/s
	Installing collected packages: requests
	Successfully installed requests-2.10.0
	>>> requests
	<module 'requests' from '/usr/home/iblis/venv/universe/lib/python3.6/site-packages/requests/__init__.py'>


``c``: import c lib via ``cffi`` (maybe work).
----------------------------------------------------------------------

Only tested with clang on FreeBSD 10.1.

.. code-block:: python

    >>> from functools import partial
    >>> from c import stdio
    Collecting cffi
    Downloading cffi-1.6.0.tar.gz (397kB)
        100% |████████████████████████████████| 399kB 2.0MB/s
    Collecting pycparser (from cffi)
    Downloading pycparser-2.14.tar.gz (223kB)
        100% |████████████████████████████████| 225kB 6.4MB/s
    Installing collected packages: pycparser, cffi
    Running setup.py install for pycparser ... done
    Running setup.py install for cffi ... done
    Successfully installed cffi-1.6.0 pycparser-2.14
    >>> cint = partial(stdio.ffi.cast, 'int')
    >>> stdio.printf(b'Hello PyCon TW %d!\n', cint(2016))
    Hello PyCon TW 2016!
    20


Hey, I got some wierd idea!
----------------------------------------------------------------------

Feel free to open issue and disscuss with folks!
We just like hacking!
