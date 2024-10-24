import pandas as pd
import numpy as np
import logging

# Set up logging
logging.basicConfig(filename='clean_data.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(input_file, output_file):
    try:
        # Load the data
        logging.info(f"Loading data from {input_file}")
        data = pd.read_csv(input_file)
        logging.info(f"Data loaded successfully. Shape: {data.shape}")

        # Step 1: Handle missing values
        # Identify columns with missing values
        missing_values = data.isnull().sum()
        logging.info(f"Missing values before cleaning: \n{missing_values}")
        
        # Drop rows where more than 50% of the columns are missing
        data = data.dropna(thresh=len(data.columns) * 0.5)
        logging.info(f"Rows with more than 50% missing values dropped. New shape: {data.shape}")
        
        # For other columns, fill missing values with mean for numerical columns
        num_columns = data.select_dtypes(include=[np.number]).columns
        data[num_columns] = data[num_columns].fillna(data[num_columns].mean())
        logging.info(f"Filled missing values in numerical columns with column mean")

        # Step 2: Remove duplicates
        duplicates = data.duplicated().sum()
        logging.info(f"Number of duplicate rows: {duplicates}")
        data = data.drop_duplicates()
        logging.info(f"Duplicates removed. New shape: {data.shape}")

        # Step 3: Correct data types
        # Ensure population column is numeric
        if 'population' in data.columns:
            data['population'] = pd.to_numeric(data['population'], errors='coerce')
            logging.info(f"Population column converted to numeric.")

        # Step 4: Handle outliers
        # For numeric columns, remove rows with values greater than 3 standard deviations from the mean
        for col in num_columns:
            mean = data[col].mean()
            std = data[col].std()
            outliers = data[(data[col] < (mean - 3 * std)) | (data[col] > (mean + 3 * std))].shape[0]
            data = data[(data[col] >= (mean - 3 * std)) & (data[col] <= (mean + 3 * std))]
            logging.info(f"Removed {outliers} outliers from column {col}")

        # Step 5: Normalize or standardize data if necessary (optional step)
        # Example: Standardize the population column
        if 'population' in data.columns:
            data['population'] = (data['population'] - data['population'].mean()) / data['population'].std()
            logging.info(f"Standardized the population column")

        # Save the cleaned data
        data.to_csv(output_file, index=False)
        logging.info(f"Cleaned data saved to {output_file}")

    except Exception as e:
        logging.error(f"Error during cleaning process: {e}")

if __name__ == "__main__":
    input_file = 'messy_population_data.csv'
    output_file = 'cleaned_population_data.csv'
    clean_data(input_file, output_file)
