from bugreport_class import BugReport
from pathlib import Path
import pytest
import os
import csv
import json


@pytest.mark.smoke
def test_to_dict(): # Testing the 'to_dict' function
    test_bug = BugReport('001', 'App crashes on login', 'High', 'Open')
    result = test_bug.to_dict()
    assert result == {'id': '001', 'title': 'App crashes on login', 'severity': 'High', 'status': 'Open'}

@pytest.mark.parametrize("severity", [ None, "", "Fatal", "Mild", "Severe"])
def test_invalid_severity(severity): # Testing for ValueError
    with pytest.raises(ValueError):
        severity_bug = BugReport('001', 'App crashes on login', severity, 'Open')

def test_init_valid_inputs():# Verify the attributes in the init def are correct
    test_report = BugReport('002', 'Login Failure', 'Critical', 'Open')
    assert test_report.bug_id == '002'
    assert test_report.title == 'Login Failure'
    assert test_report.severity == 'Critical'
    assert test_report.status == 'Open'

@pytest.mark.smoke
def test_does_json_exist(): # Testing for json file creation
    json_path = Path(__file__).parent /'test_file.json'
    assert json_path.is_file(), f'Does not exist at: {json_path}'

def test_json_structure(): # Verify the json file is a list of dictionaries
    json_path = Path(__file__).parent / 'test_file.json'

    with open(json_path, 'r') as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)

@pytest.mark.smoke
def test_valid_csv():
    file_path = Path(__file__).parent / 'bugs_report.csv'
    assert file_path.is_file()

def test_valid_headers():
    with open(Path(__file__).parent / 'bugs_report.csv', 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)
        assert 'ID' in rows[0]
        assert 'Title' in rows[0]
        assert 'Severity' in rows[0]
        assert 'Status' in rows[0]

def test_is_csv_empty():
    file_path = Path(__file__).parent / 'bugs_report.csv'
    assert os.path.getsize(file_path) > 0

def test_dict_bug_not_empty():
    test_bug = BugReport('001', 'App crashes on login', 'High', 'Open')
    assert len(test_bug.to_dict()) > 0


def test_dict_bug_keys():
    test_bug = BugReport('001', 'App crashes on login', 'High', 'Open').to_dict()
    required_keys = {'id', 'title', 'severity', 'status'}
    assert required_keys.issubset(test_bug.keys())

