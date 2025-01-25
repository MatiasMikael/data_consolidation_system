import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection information
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Build the connection string
connection_string = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Define log file path
LOG_FOLDER = "5_logs"
os.makedirs(LOG_FOLDER, exist_ok=True)
LOG_FILE = os.path.join(LOG_FOLDER, "test_sql_connection.log")

def log_message(message):
    """Logs a message to the log file and prints it to the console."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{message}\n")
    print(message)

# SQL query to fetch data
query = "SELECT * FROM asiakas_taulu;"

# Fetch data from the database
try:
    engine = create_engine(connection_string)
    with engine.connect() as connection:
        log_message("Connecting to the database...")
        data = pd.read_sql(query, connection)
        log_message("Data fetched successfully:")
        log_message(data.head().to_string())  # Log first rows
        print(data.head())  # Print first rows to the console
except Exception as e:
    log_message(f"Error: {e}")