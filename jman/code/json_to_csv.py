import csv
import json

data_path = "./data/"
data_files = ["disaster_data.preprocessing","non_disaster_data.preprocessing"]

input_type = ".json"
output_type = ".csv"


for data_file in data_files:
	with open(data_path + data_file + input_type, "r", newline="") as input_file, \
			open(data_path + data_file + output_type, "w", newline="") as output_file:
		data = []
		for line in input_file:
			#print("line",line)
			datum = json.loads(line)
			#print("datum",datum)
			data.append(datum)
		csvwriter = csv.writer(output_file)
		csvwriter.writerow(data[0].keys())
		for line in data:
			csvwriter.writerow(line.values())
