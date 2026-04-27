# Week 4 — Advanced Pytest: Fixtures, Parametrize & Conftest

## Overview
Week 4 focused on advanced pytest concepts — fixtures, conftest.py, fixture scope, teardown with yield, deeper @pytest.mark.parametrize usage, and custom test markers. The Week 3 test suite was refactored to eliminate manual setup repetition.

## What Was Built
- Refactored test_to_dict, test_init_valid_inputs, test_dict_bug_not_empty, and test_dict_bug_keys to use the fixture

- Parametrized test_to_dict across 3 valid BugReport inputs with expected dictionary assertions

- Added regression marker to pytest.ini and applied it to relevant tests

## Struggles and Resolutions
- Practice files pushed to GitHub — absent .gitignore caused unintended files to be tracked. Resolved with git rm --cached and a properly configured .gitignore

- Missing fixture parameter in function signatures — forgetting to add bug_report to test signatures caused FixtureFunctionDefinition errors. Resolved by reading the error output carefully

## How to Run the Tests
- Activate the virtual environment from repo root
`venv\Scripts\activate`

- Navigate to week 4 folder
`cd week-04-advanced_pytest`

- Run full suite
`pytest test_bug_report.py -v`

- Run smoke tests only
`pytest test_bug_report.py -v -m "smoke"`

- Run regression tests only
`pytest test_bug_report.py -v -m "regression"`