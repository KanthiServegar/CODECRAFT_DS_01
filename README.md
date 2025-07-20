# CODECRAFT_DS_01
World Population Data Analysis (2022)
This project performs data analysis and visualization using the World Bank's population dataset. The analysis focuses on the total population of countries in the year 2022.

📁 Dataset
The dataset used is from the World Bank:
File Name: API_SP.POP.TOTL_DS2_en_csv_v2_5830.csv
It contains total population data for various countries from 1960 to 2022.

📊 Features of the Project
Data Cleaning:
The first few rows of the CSV file (notes and metadata) are skipped using skiprows=4.

Filtering for 2022:
Extracts population data for each country for the year 2022, removing any rows with missing values.

Top 10 Populated Countries:
Sorts and displays the 10 most populated countries in 2022.

Visualizations:

📈 Bar Chart: Displays the top 10 most populated countries.

📉 Histogram: Shows the distribution of population sizes across all countries.

🧰 Technologies Used
Python

Pandas – for data manipulation

Matplotlib – for data visualization

📌 How to Run
Make sure you have Python installed.

Install the required libraries if not already installed:

pip install pandas matplotlib
Place the dataset file (API_SP.POP.TOTL_DS2_en_csv_v2_5830.csv) in the same directory as the script.

Run the Python script
