.. image:: https://github.com/eng-tools/engformat/actions/workflows/ci.yaml/badge.svg
   :target: https://github.com/eng-tools/engformat/actions/workflows/ci.yaml
   :alt: CI Status

.. image:: https://github.com/eng-tools/engformat/actions/workflows/release.yaml/badge.svg
   :target: https://github.com/eng-tools/engformat/actions/workflows/release.yaml
   :alt: Release Status

.. image:: https://img.shields.io/pypi/v/engformat.svg
   :target: https://pypi.python.org/pypi/engformat
   :alt: PyPI version

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/eng-tools/engformat/blob/master/LICENSE
   :alt: License

*********
engformat
*********

This Python project contains tools to present work according to the engineering
standard format.

Supported Python Versions
=========================

engformat supports the latest stable Python plus the previous three releases.
The current support window is **Python 3.10 to 3.13**.

This policy is reviewed quarterly and updated when a new Python release becomes
stable.

Local Development Setup
=======================

1. Create and activate a virtual environment:

   .. code-block:: powershell

      python -m venv .venv
      .\.venv\Scripts\Activate.ps1

2. Install dependencies:

   .. code-block:: powershell

      python -m pip install --upgrade pip
      python -m pip install -r requirements.txt -r test-requirements.txt
      python -m pip install -e .

3. Run tests:

   .. code-block:: powershell

      python -m pytest

Release Checklist
=================

1. Update ``engformat/__about__.py`` with the new version.
2. Confirm CI passes for Python 3.10, 3.11, 3.12, and 3.13.
3. Build distributions locally:

   .. code-block:: powershell

      python -m pip install -r deploy-requirements.txt
      python -m build

4. Push a version tag to trigger the trusted publishing workflow.
