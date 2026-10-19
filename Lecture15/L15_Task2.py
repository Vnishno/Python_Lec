import csv

with open("titanic.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    survivors = []
    for row in reader:
        if int(row['Survived']) == 1:
            survivors.append(row)

with open("survived.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(survivors)