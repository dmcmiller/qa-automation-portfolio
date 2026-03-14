import csv

severity_level = input('Please select a severity level: ').lower()
matching_bugs = []
with open('bugs_report.csv', 'r', encoding='utf-8-sig') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        if row['Severity'] == severity_level:
            matching_bugs.append(row)
            print(f"Bug Name: {row['ID']} | Description: {row['Description']}. | The "
                  f"status is {row['Status']} with a severity of {row['Severity']}.")
    if not matching_bugs:
        print('You entered an incorrect severity level.')
    else:
        print(f"There are {len(matching_bugs)} bugs with severity: {severity_level}")

