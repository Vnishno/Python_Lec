import csv

def filter_and_save_companies(input_file, output_file):

    headers = ["Name", "Industry", "Number of employees"]
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        filtered_companies = []
        for row in reader:
            if int(row["Number of employees"]) > 1000:
                filtered_companies.append({
                    "Name": row["Name"],
                    "Industry": row["Industry"],
                    "Number of employees": row["Number of employees"]
                })

    with open(output_file, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(filtered_companies)

filter_and_save_companies("ssl_companies.csv", "sorted_companies.csv")