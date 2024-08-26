import pandas as pd
import csv
import datetime as datetime

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category","description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS) # DataFrame - Object within Pandas which allows us to access different rows and columns in a CSV file
            df.to_csv(cls.CSV_FILE, index=False) 
        
    @classmethod
    def add_entry(cls, date, amount, category, description):
        # Storing the new entry into a Dictonary!
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added SUCCESSFULLY!")

CSV.initialize_csv()
CSV.add_entry("25-08-2024", 123.45, "Income", "Salary")

 