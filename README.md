# sales-data-cleaning
# Amazon Sales Data Cleaning

## Objective:
The project involves cleaning and preparing a raw Amazon sales dataset, addressing issues like missing values, duplicates, inconsistent formats, and ensuring the dataset is ready for analysis.

## Tools Used:
- **Python (Pandas)** for data cleaning and transformation
- **Excel** for handling and exploring the dataset (if required)

## Key Steps Taken:
1. **Handled Missing Values**:
   - Missing values were either dropped or filled with the mean/median where applicable.
   
2. **Removed Duplicates**:
   - Duplicate rows were identified and removed based on `Order ID`.
   
3. **Standardized Text Values**:
   - Text fields like `Product Name`, `Customer Information`, and `Country` were converted to lowercase and standardized.
   
4. **Converted Date Formats**:
   - The `Date` column was converted to a consistent `dd-mm-yyyy` format.
   
5. **Renamed Columns**:
   - Columns were renamed to ensure consistency (e.g., lowercase, no spaces).
   
6. **Checked and Fixed Data Types**:
   - Ensured that `Quantity Sold` was an integer, `Price` was a float, and `Date` was in datetime format.

## Deliverables:
- Cleaned dataset saved as `amazon_sales_cleaned.csv`.
- A detailed explanation of the cleaning steps taken.

## Usage:
Clone the repository and follow the instructions in the script to clean your own Amazon sales dataset.
