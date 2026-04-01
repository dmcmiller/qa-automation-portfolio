# Build a BugReport class with attributes id, title, severity, 
# status and methods to_dict and from_csv. Create 5 instances 
# and serialize them to a JSON file.
import csv
import json

class BugReport:
    def __init__(self, bug_id, title, severity, status):
        if severity is None:
            raise ValueError('Severity can NOT be None.')
        self.bug_id = bug_id
        self.title = title
        self.severity = severity
        self.status = status


    def to_dict(self):
        my_dict = {'id': self.bug_id, 'title': self.title, 'severity': self.severity, 'status': self.status}
        return my_dict
    
    @classmethod
    def from_csv(cls, row):
        return cls(row['ID'], row['Title'], row['Severity'], row['Status'])

bugs = []
try:
    with open('C:/Users/daron/qa-automation-portfolio/week-03-pytest/bugs_report.csv', 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            bug = BugReport.from_csv(row)  # each row becomes a BugReport instance
            bugs.append(bug)
except FileNotFoundError as error:
    print(error)
    exit()

dict_bugs = [bug.to_dict() for bug in bugs]

with open('C:/Users/daron/qa-automation-portfolio/week-03-pytest/test_file.json', 'w') as json_file:
     json.dump(dict_bugs, json_file, indent=4)

print(dict_bugs)


