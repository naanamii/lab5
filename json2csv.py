import json
import csv
import sys
import os

def json_to_csv(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        root_name = os.path.splitext(os.path.basename(json_file))[0]
        csv_file = f"{root_name}.csv"

        with open(csv_file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            if isinstance(data, dict):
                csvwriter.writerow(data.keys())
                csvwriter.writerow(data.values())
            elif isinstance(data, list):
                csvwriter.writerow(data[0].keys())
                for item in data:
                    csvwriter.writerow(item.values())

        print(f"CSV файл успешно создан: {csv_file}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите имя json файла в качестве аргумента")
    else:
        json_file = sys.argv[1]
        json_to_csv(json_file)