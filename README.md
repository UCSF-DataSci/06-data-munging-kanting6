import pandas as pd

# Load the dataset
data = pd.read_csv('/Users/kankantingting/Documents/messy_population_data.csv') 

# Display the first few rows to get an overview of the dataset
print(data.head())

# Get summary of the data
print(data.info())

# Get summary statistics for numeric columns
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Check for duplicate rows
print(data.duplicated().sum())

# Check for unique values in categorical columns
print(data['Country'].value_counts()) 
Missing Data:

income_groups: 6,306 missing entries (around 5%).
age: 6,223 missing entries.
gender: 5,907 missing entries.
year: 6,202 missing entries.
population: 6,340 missing entries.
Data Types:

Most columns (age, gender, year, population) are stored as float64, which may be unnecessary for categorical data like gender and year.
Gender Representation:

The gender column uses numeric values (e.g., 1.0, 3.0). The value 3.0 seems irregular for a binary gender representation.
Age:

There are records where age is 0, which could represent newborns or invalid data.[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16596636)
