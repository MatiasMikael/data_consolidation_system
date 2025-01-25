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
LOGS_FOLDER = "5_logs"

# Logging setup
LOG_FILE = os.path.join(LOGS_FOLDER, "fetch_data.log")
os.makedirs(LOGS_FOLDER, exist_ok=True)

def log_message(message):
    """Logs a message to the log file and prints it to the console."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{message}\n")
    print(message)

def fetch_csv(file_path):
    """Fetches data from a CSV file and returns it as a DataFrame."""
    try:
        log_message(f"Fetching CSV data from {file_path}...")
        csv_data = pd.read_csv(file_path)
        log_message(f"CSV data loaded successfully: {file_path}")
        return csv_data
    except Exception as e:
        log_message(f"Error loading CSV file {file_path}: {e}")
        return None

def fetch_json(file_path):
    """Fetches data from a JSON file and returns it as a DataFrame."""
    try:
        log_message(f"Fetching JSON data from {file_path}...")
        with open(file_path, "r") as file:
            json_data = pd.read_json(file)
        log_message(f"JSON data loaded successfully: {file_path}")
        return pd.DataFrame(json_data)
    except Exception as e:
        log_message(f"Error loading JSON file {file_path}: {e}")
        return None

def fetch_sql(query):
    """Fetches data from a SQL database and returns it as a DataFrame."""
    connection_string = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    try:
        log_message("Connecting to the database...")
        engine = create_engine(connection_string)
        with engine.connect() as connection:
            log_message("Connected successfully. Executing query...")
            sql_data = pd.read_sql(query, connection)
        log_message("SQL data fetched successfully.")
        return sql_data
    except Exception as e:
        log_message(f"Error fetching data from SQL database: {e}")
        return None

def main():
    # Example files to load
    csv_file = os.path.join(DATA_FOLDER, "data1.csv")
    json_file = os.path.join(DATA_FOLDER, "data2.json")

    # SQL query
    query = "SELECT * FROM asiakas_taulu;"

    # Fetch data
    csv_data = fetch_csv(csv_file)
    json_data = fetch_json(json_file)
    sql_data = fetch_sql(query)

    # Placeholder for further processing or saving data
    if csv_data is not None:
        log_message(f"CSV data preview:\n{csv_data.head()}")
    if json_data is not None:
        log_message(f"JSON data preview:\n{json_data.head()}")
    if sql_data is not None:
        log_message(f"SQL data preview:\n{sql_data.head()}")

if __name__ == "__main__":
    main()