========
Overview
========

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/coddingtonbear/boox-annotation-parser/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/coddingtonbear/boox-annotation-parser/compare/v0.1.0...master



.. end-badges

Parse annotation file exports from your Boox device, and transform them into JSON, YAML, or whatever you want.

* Free software: MIT license

Installation
============

::

    pip install boox-annotation-parser

You can also install the in-development version with::

    pip install https://github.com/coddingtonbear/boox-annotation-parser/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import boox_annotation_parser
    boox_annotation_parser.longest()


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
