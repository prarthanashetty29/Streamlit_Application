import pandas as pd
import sqlite3
import os

# Absolute paths for the CSV file and the SQLite database
csv_file_path = 'C:/Users/prart/Desktop/loan_db.csv'  # Update to your actual CSV file path
db_file_path = 'C:/Users/prart/TEXTTOSQL/loan_db.db'

# Check if the CSV file exists
if not os.path.isfile(csv_file_path):
    print(f"The file {csv_file_path} does not exist.")
else:
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Connect to the SQLite database using the absolute path
        conn = sqlite3.connect(db_file_path)

        # Write the DataFrame to the SQLite database
        df.to_sql('loan_db', conn, if_exists='replace', index=False)

        # Close the connection
        conn.close()

        print(f"The database {db_file_path} has been created with the data from the CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")
