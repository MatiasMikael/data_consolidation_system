import pandas as pd
import os

# Define folder paths
RESULTS_FOLDER = "3_results"
LOGS_FOLDER = "5_logs"

# Logging setup
LOG_FILE = os.path.join(LOGS_FOLDER, "clean_data.log")
os.makedirs(LOGS_FOLDER, exist_ok=True)

def log_message(message):
    """Logs a message to the log file and prints it to the console."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{message}\n")
    print(message)

def clean_data(input_file, output_file):
    """Cleans the combined data and saves the cleaned version."""
    try:
        log_message(f"Loading combined data from {input_file}...")
        data = pd.read_csv(input_file)
        log_message("Data loaded successfully.")

        # Rename and select columns
        cleaned_data = data.rename(columns={
            "nimi_x": "nimi",
            "ikä": "ika",
            "tulot_x": "tulot",
            "kaupunki_x": "kaupunki",
            "kulutus_x": "kulutus"
        })[["id", "nimi", "ika", "tulot", "kaupunki", "kulutus"]]

        log_message("Data cleaned successfully.")
        log_message(f"Cleaned data preview:\n{cleaned_data.head()}")

        # Save cleaned data
        cleaned_data.to_csv(output_file, index=False)
        log_message(f"Cleaned data saved to {output_file}")
    except Exception as e:
        log_message(f"Error during data cleaning: {e}")

def main():
    input_file = os.path.join(RESULTS_FOLDER, "combined_data.csv")
    output_file = os.path.join(RESULTS_FOLDER, "combined_data_cleaned.csv")

    if not os.path.exists(input_file):
        log_message(f"Error: Input file {input_file} does not exist.")
        return

    clean_data(input_file, output_file)

if __name__ == "__main__":
    main()