import csv
from pprint import pprint

with open("sample_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        pprint(line)


# Read file as a dictionary
with open("sample_data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        pprint(line)
