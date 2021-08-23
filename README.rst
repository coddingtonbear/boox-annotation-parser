======================
Boox Annotation Parser
======================

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |version| image:: https://img.shields.io/pypi/v/boox-annotation-parser.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/boox-annotation-parser

.. |wheel| image:: https://img.shields.io/pypi/wheel/boox-annotation-parser.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/boox-annotation-parser

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/boox-annotation-parser.svg
    :alt: Supported versions
    :target: https://pypi.org/project/boox-annotation-parser

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/boox-annotation-parser.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/boox-annotation-parser

.. |commits-since| image:: https://img.shields.io/github/commits-since/coddingtonbear/boox-annotation-parser/v0.1.2.svg
    :alt: Commits since latest release
    :target: https://github.com/coddingtonbear/boox-annotation-parser/compare/v0.1.2...master



.. end-badges

Parse annotation file exports from your Onyx Boox device, and transform them into JSON, YAML, or whatever you want.

* Free software: MIT license

Installation
============

::

    pip install boox-annotation-parser

You can also install the in-development version with::

    pip install https://github.com/coddingtonbear/boox-annotation-parser/archive/master.zip


Documentation
=============

To use the project from the command-line
----------------------------------------

Options:

- ``--input``: (Default: 'stdin') The path to your Boox annotation export file.  If unspecified, reads from stdin.
- ``--output``: (Default: 'stdout') The path to where you'd like your output written to.  If unspecified, writes to stdout.
- ``--format``: (Default: 'yaml') The format you'd like your annotations written out in.  Options include:
  - ``yaml``
  - ``json``
  - ``nljson``

::

    boox-annotation-parser --input=/path/to/boox/export.txt --output=/path/to/write/output/to --format=yaml

To use the project as a library
-------------------------------

.. code-block:: python

    from boox_annotation_parser import parser

    with open('/path/to/boox/export.txt', 'r') as inf:
        parsed = parser.get_annotations(inf)


Development
===========

To run the tests run::

    pytest
