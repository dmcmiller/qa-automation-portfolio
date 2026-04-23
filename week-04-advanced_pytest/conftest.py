import pytest
from bugreport_class import BugReport


@pytest.fixture
def bug_report():
    report = BugReport('001', 'App crashes on login', 'High', 'Open')
    yield report
    print('Test is being cleaned up')