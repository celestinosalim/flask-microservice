import csv, json

#reading csv adding data to dict
data = {}
voters = []

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        voters.append(line)
        data['voters'] = voters
        

#write data to json file.
with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))
