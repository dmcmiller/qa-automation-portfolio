from bugreport_class import BugReport
from pathlib import Path
import pytest
import os
import csv
import json




@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("bug_id, title, severity, status, expected", [
    ('001', 'App crashes on login', 'Critical', 'Open', {'id': '001', 'title': 'App crashes on login', 'severity': 'Critical', 'status': 'Open'}),
    ('002', 'Incorrect password error loop', 'Critical', 'in progress', {'id': '002', 'title': 'Incorrect password error loop', 'severity': 'Critical', 'status': 'in progress'}),
    ('003', 'Profile picture fails', 'Medium', 'Open', {'id': '003', 'title': 'Profile picture fails', 'severity': 'Medium', 'status': 'Open'})
])
def test_to_dict(bug_id, title, severity, status, expected):
    report = BugReport(bug_id, title, severity, status)
    assert report.to_dict() == expected

@pytest.mark.parametrize("severity", [ None, "", "Fatal", "Mild", "Severe"])
def test_invalid_severity(severity): # Testing for ValueError
    with pytest.raises(ValueError):
        severity_bug = BugReport('001', 'App crashes on login', severity, 'Open')

def test_init_valid_inputs(bug_report):# Verify the attributes in the init def are correct
    assert bug_report.bug_id == '001'
    assert bug_report.title == 'App crashes on login'
    assert bug_report.severity == 'High'
    assert bug_report.status == 'Open'

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

@pytest.mark.regression
def test_is_csv_empty():
    file_path = Path(__file__).parent / 'bugs_report.csv'
    assert os.path.getsize(file_path) > 0

def test_dict_bug_not_empty(bug_report):
    assert len(bug_report.to_dict()) > 0


def test_dict_bug_keys(bug_report):
    required_keys = {'id', 'title', 'severity', 'status'}
    assert required_keys.issubset(bug_report.to_dict().keys())

