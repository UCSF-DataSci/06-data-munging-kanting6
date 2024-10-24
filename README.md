import pandas as pd
data = pd.read_csv('/Users/kankantingting/Documents/messy_population_data.csv') 
print(data.head(data))

print(data.info(data))

print(data.describe(data))

print(data.isnull().sum(data))

print(data.duplicated().sum(data))

print(data['Country'].value_counts(data)) 

#Exploratory Data Analysis (EDA) Issues Results:

1) 

income_groups: 6,306 missing entries (around 5%).
age: 6,223 missing entries.
gender: 5,907 missing entries.
year: 6,202 missing entries.
population: 6,340 missing entries.
Data Types:

2)
Most columns (age, gender, year, population) are stored as float64, which may be unnecessary for categorical data like gender and year.
Gender Representation:

3)
The gender column uses numeric values (e.g., 1.0, 3.0). The value 3.0 seems irregular for a binary gender representation.

4) 
Age:
There are records where age is 0, which could represent newborns or invalid data.


# Data Cleaning Process

## Input Data: `messy_population_data.csv`
The dataset contains population data with issues such as missing values, duplicates, inconsistent data types, and outliers. This script addresses these issues systematically.

### Cleaning Process:

1. **Missing Values**:
   - **Method**: Rows with more than 50% missing values are dropped. For other missing values in numeric columns, the column mean is used to fill in the gaps.

2. **Duplicate Rows**:
   - **Method**: Identified and removed duplicate rows.

3. **Data Type Correction**:
   - **Method**: Converted the `population` column to a numeric data type.

4. **Outlier Removal**:
   - **Method**: Removed rows with values greater than 3 standard deviations from the mean in numeric columns.

5. **Standardization** (Optional):
   - **Method**: Standardized the `population` column by converting values to z-scores (mean of 0, standard deviation of 1).

### Error Handling and Logging:
- The script includes error handling to log any issues encountered during the cleaning process. A log file (`clean_data.log`) is generated for tracking purposes.
- Errors such as missing input files or issues during the cleaning process will be captured and documented in the log.

## Output Data: `cleaned_population_data.csv`

The cleaned dataset has improved data quality, with missing values addressed, duplicates removed, correct data types, and outliers handled. 




