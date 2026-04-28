# Week 6 Capstone Pytest Test Suite

## Prerequisites
- Python 3.12.4 or higher
- pytest
- requests
- pytest-html plugin

## Installation
1. Clone the repository
   git clone https://github.com/dmcmiller/qa-automation-portfolio
2. Navigate to the week 6 folder
   cd week-06-capstone
3. Install dependencies
   pip install -r requirements.txt

## Overview
Week 6 focused on creating a test suite to cover a varied range of tests involving https://jsonplaceholder.typicode.com/
These tests can be split between three categories: Status Code Validation, Schema Validation, and Data Validation
This week combined the efforts of the past few weeks, from basic python knowledge, Pytest Fixtures, Markers Parametrization.


## How to Run the Tests
- Run the full test `pytest .\test_api.py -v`
- Run the parametrized tests `pytest -v -k "test_user_values_not_empty or test_post_response"`
- Run the various marked tests `pytest .\test_api.py -v -m {marker}` - marker being one of four options: smoke, status, schema, data

## Generate HTML report
- Run the following to generate a Pytest HTML report `pytest --html=api_test_results.html -v`