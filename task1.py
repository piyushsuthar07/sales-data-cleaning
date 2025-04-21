import pandas as pd

data = pd.read_csv("D:\\study\\intern\\task 1\\amazon.csv")

#inspect the data
print(data.head)
print(data.info())

# Handle Missing Values
print(data.isnull().sum())
print(data.dropna())

#Remove Duplicates
print(data.drop_duplicates())

#Standardize Text Values
data['product_name'] = data['product_name'].str.lower().str.strip()
print(data.head)

#there is no date in my data
#data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

#Rename Columns to be Clean and Uniform
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Save the cleaned dataset to a new file
data.to_csv('amazon_sales_cleaned.csv', index=False)
