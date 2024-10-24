import pandas as pd
import numpy as np
import logging
import os

# Setup logging
logging.basicConfig(
    filename='clean_data.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}. Exception: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        logging.error(f"No data found in file: {file_path}. Exception: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading data from {file_path}: {e}")
        raise

def clean_data(df):
    """Clean the loaded dataframe."""
    # 1. Drop duplicate rows
    df.drop_duplicates(inplace=True)
    logging.info(f"Removed duplicate rows. New shape: {df.shape}")

    # 2. Handle missing values
    # For 'income_groups', replace missing values with 'Unknown'
    if 'income_groups' in df.columns:
        df['income_groups'].fillna('Unknown', inplace=True)
        logging.info(f"Filled missing values in 'income_groups' with 'Unknown'.")

    # For 'age', replace missing values with the median age
    if 'age' in df.columns:
        median_age = df['age'].median()
        df['age'].fillna(median_age, inplace=True)
        logging.info(f"Filled missing values in 'age' with median: {median_age}")

    # For 'gender', replace missing values with 'Not Specified'
    if 'gender' in df.columns:
        df['gender'].fillna('Not Specified', inplace=True)
        logging.info("Filled missing values in 'gender' with 'Not Specified'.")

    # For 'year', replace missing values with the mode (most frequent year)
    if 'year' in df.columns:
        most_frequent_year = df['year'].mode()[0]
        df['year'].fillna(most_frequent_year, inplace=True)
        logging.info(f"Filled missing values in 'year' with mode: {most_frequent_year}")

    # For 'population', replace missing values with the median population
    if 'population' in df.columns:
        median_population = df['population'].median()
        df['population'].fillna(median_population, inplace=True)
        logging.info(f"Filled missing values in 'population' with median: {median_population}")

    # 3. Correct data types (e.g., ensure 'year' is an integer)
    try:
        df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
        logging.info("Converted 'year' column to integer.")
    except Exception as e:
        logging.error(f"Error converting 'year' to integer: {e}")

    # 4. Strip whitespace from string columns
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    logging.info("Stripped whitespace from string columns.")

    # 5. Remove rows with unrealistic population values (e.g., population < 0)
    df = df[df['population'] >= 0]
    logging.info(f"Removed rows with unrealistic population values. New shape: {df.shape}")

    return df

def save_cleaned_data(df, output_path):
    """Save the cleaned dataframe to a CSV file."""
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Cleaned data saved to {output_path}.")
    except Exception as e:
        logging.error(f"An error occurred while saving cleaned data to {output_path}: {e}")
        raise

if __name__ == "__main__":
    # Define input and output file paths
    input_file = os.path.expanduser("~/Documents/messy_population_data.csv")
    output_file = os.path.expanduser("~/Documents/cleaned_population_data.csv")

    # Load the data
    try:
        df = load_data(input_file)

        # Clean the data
        cleaned_df = clean_data(df)

        # Save the cleaned data
        save_cleaned_data(cleaned_df, output_file)
        print("Data cleaning completed successfully!")
    except Exception as e:
        logging.critical(f"Data cleaning failed due to an error: {e}")
        print(f"Data cleaning failed. Check the log file for details.")
