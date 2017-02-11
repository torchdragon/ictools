Release History
===============

`Next Release`_
---------------
* added "metadata" element to all JSON output.
* switched to using :mod:`argparse` for parsing.  The only observable effect
  of this is that ``--help`` and ``--version`` are now supported.
* added ``--format`` command line option.
* added ``--quiet`` and ``--verbose`` command line options.
* changed default diagnostic level from INFO -> WARNING.

`0.1.0`_ (23-Jan-2017)
----------------------
* added :ref:`scan_hipchat_room` utility
* added :ref:`list_pagerduty_incidents` utility

.. _Next Release: https://github.com/dave-shawley/ictools/compare/0.1.0...HEAD
.. _0.1.0: https://github.com/dave-shawley/ictools/compare/0.0.0...0.1.0
