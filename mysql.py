import mysql.connector
import csv

# Database connection details
mydb = mysql.connector.connect(
  host="your_database_host",
  user="your_username",
  password="your_password",
  database="your_database_name"
)

cursor = mydb.cursor()

# CSV file path
csv_file_path = "path/to/your/csv_file.csv"

# Table name in the database
table_name = "your_table_name"

# Read and insert data from CSV
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row if it exists

    for row in csv_reader:
        # Assuming the columns in the CSV match the columns in the database table
        query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})"
        cursor.execute(query, row)

mydb.commit()
cursor.close()
mydb.close()
