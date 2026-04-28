# Week 6 Capstone Pytest Test Suite

## Overview
Week 6 focused on creating a test suite to cover a varied range of tests involving https://jsonplaceholder.typicode.com/
These tests can be split between three categories: Status Code Validation, Schema Validation, and Data Validation
This week combined the efforts of the past few weeks, from basic python knowledge, Pytest fixutures, Markers Parametrization, and the basics of Git and GitHub.


## How to Run the Tests
- Run the full test `pytest .\test_api.py -v`
- Run the parametrized tests `pytest -v -k "test_user_values_not_empty or test_post_response"`
- Run the various marked tests `pytest .\test_api.py -v -m {marker}` - marker being one of four options: smoke, status, schema, data