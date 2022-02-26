import csv
with open("students.csv",'r') as csv_files:
    reader = csv.reader(csv_files)
    rows = []

    for rec in reader:
        rows.append(rec)
print(rows)    