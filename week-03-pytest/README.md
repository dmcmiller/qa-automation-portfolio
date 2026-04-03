
# Week 3 — Pytest Suite

## Overview
bugreport_class.py takes a row
from the bug report sheet and creates a BugReport instance. The BugReport instances
are then serialized into a json file. 
The test_bug_report test suite tests the functionality of the class.

## Setup

1. Clone the repo
2. Create a virtual environment:
   python -m venv venv
3. Activate it:
   venv\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt
5. Run the tests:
   pytest test_bug_report.py -v

## Running Tests
Run the full test suite by running: pytest test_bug_report.py -v
In order to only run the smoke tests, run the following: pytest test_bug_report.py -v -m "smoke"



## Test Coverage
The test suite covers basic class functionality, input validation and file checks
- `test_to_dict()` tests for correct keys and values
- `test_invalid_severity` raises a ValueError if value is one of five items
- `test_init_valid_inputs` verifies the attributes in the init
- `test_does_json_exist` verifies the creation of the json file, while `test_json_structure` then verifies the json consists of a list of dictionaries
- `test_valid_csv` verifies the csv is in fact a file, `test_valid_headers` compliments this by verifying the headers of the csv
- `test_is_csv_empty` tests for an empty csv file
- `test_dict_bug_not_empty` verifies the dictionary created by the `to_dict()` method doesn't create an empty dictionary
- test_dict_bug_keys verifies the dictionary created by `to_dict()` has the required keys

