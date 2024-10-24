import pandas as pd
data = pd.read_csv('/Users/kankantingting/Documents/messy_population_data.csv') 
print(data.head(data))
print(data.info(data))
print(data.describe(data))
print(data.isnull().sum(data))
print(data.duplicated().sum(data))
print(data['Country'].value_counts(data)) 

#Missing Data:
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
There are records where age is 0, which could represent newborns or invalid data.[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16596636)
