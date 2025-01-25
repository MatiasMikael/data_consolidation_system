import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection information
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Define folder paths
DATA_FOLDER = "2_data"
RESULTS_FOLDER = "3_results"
LOGS_FOLDER = "5_logs"

# Logging setup
LOG_FILE = os.path.join(LOGS_FOLDER, "combine_data.log")
os.makedirs(LOGS_FOLDER, exist_ok=True)

def log_message(message):
    """Logs a message to the log file and prints it to the console."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{message}\n")
    print(message)

def fetch_sql_data():
    """Fetch SQL data directly from the database."""
    try:
        log_message("Fetching SQL data from the database...")
        connection_string = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(connection_string)
        with engine.connect() as connection:
            query = "SELECT * FROM asiakas_taulu;"
            sql_data = pd.read_sql(query, connection)
        log_message("SQL data loaded successfully:")
        log_message(f"{sql_data.head()}")
        return sql_data
    except Exception as e:
        log_message(f"Error fetching SQL data: {e}")
        return None

def main():
    try:
        # Load CSV data
        csv_file = os.path.join(DATA_FOLDER, "data1.csv")
        log_message(f"Loading CSV data from {csv_file}...")
        csv_data = pd.read_csv(csv_file)
        log_message(f"CSV data loaded successfully:\n{csv_data.head()}")

        # Load JSON data
        json_file = os.path.join(DATA_FOLDER, "data2.json")
        log_message(f"Loading JSON data from {json_file}...")
        json_data = pd.read_json(json_file)
        log_message(f"JSON data loaded successfully:\n{json_data.head()}")

        # Fetch SQL data
        sql_data = fetch_sql_data()
        if sql_data is None:
            log_message("Error: SQL data could not be loaded. Exiting.")
            return

        # Combine CSV and JSON data on 'id'
        combined_data = pd.merge(csv_data, json_data, on="id", how="inner")
        log_message("Combined CSV and JSON data successfully.")

        # Add SQL data to the combined DataFrame
        combined_data = pd.merge(combined_data, sql_data, on="id", how="inner")
        log_message("Added SQL data to the combined DataFrame successfully.")

        # Save the combined data to results folder
        os.makedirs(RESULTS_FOLDER, exist_ok=True)
        output_file = os.path.join(RESULTS_FOLDER, "combined_data.csv")
        combined_data.to_csv(output_file, index=False)
        log_message(f"Combined data saved to {output_file}")

    except Exception as e:
        log_message(f"Error during data combination: {e}")

if __name__ == "__main__":
    main()