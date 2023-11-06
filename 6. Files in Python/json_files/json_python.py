import json
from pprint import pprint

with open("json_file.txt", "r") as my_file:
    file_content = json.load(my_file)  # read file and turn it to dictonary

# loads convert json to dictionary


pprint(file_content["people"][0])

cars = [{"brand": "Tata", "model": "Fortuner"}, {"brand": "Suzuki", "model": "Swift"}]

with open("write_json.txt", "w") as write_file:
    json.dump(cars, write_file)
