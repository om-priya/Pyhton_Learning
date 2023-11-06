import csv

my_dict = [
    {"Passenger": "1", "Id": "0", "Survived": "1"},
    {"Passenger": "2", "Id": "1", "Survived": "1"},
    {"Passenger": "3", "Id": "2", "Survived": "3"},
]

fields = ["Passenger", "Id", "Survived"]

with open("new_csv_file.csv", "w") as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fields, delimiter="\t")

    writer.writeheader()

    writer.writerows(my_dict)
