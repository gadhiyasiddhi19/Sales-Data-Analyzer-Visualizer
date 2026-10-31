# Sales Data Analyzer & Visualizer

**Author: Siddhi Gadhiya**

---

## 📌 Project Overview

**Sales Data Analyzer & Visualizer** is a menu-driven Python project developed to analyze and visualize sales data using Pandas, NumPy, Matplotlib, and Seaborn.

It allows users to load CSV datasets, explore and manipulate data, handle missing values, perform mathematical and statistical operations, and visualize sales information using different types of charts.

The project provides an interactive menu through which users can perform various data analysis and visualization operations.

---

## 🚀 Features

- Load sales data from CSV files.
- Explore dataset structure and contents.
- Perform mathematical operations using NumPy.
- Combine and split DataFrames.
- Search, sort, and filter records.
- Perform aggregate functions.
- Handle missing values and duplicate records.
- Convert data types.
- Generate descriptive statistics.
- Create pivot tables.
- Perform GroupBy and Transform operations.
- Reindex DataFrames and rename columns.
- Generate different types of visualizations.
- Save generated charts as image files.

## 📂 Project Structure

```text
Project-9/
│
├── SalesDataAnalyzer.py
├── sales_data.csv
├── README.md
├── product_sales.png
└── output.png
```

## 🛠️ Technologies Used

- Python 3.14.6
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code
- Git
- GitHub

---

## ⚙️ Program Operations Explained

### 1. Load Dataset

This operation loads a sales dataset from a CSV file into a Pandas DataFrame.

- **`pd.read_csv()`** – Reads the CSV file and stores its data in a DataFrame.
- Displays a success message when the dataset is loaded successfully.
- Exception handling manages errors that may occur while loading the file.

### 2. Explore Data

This operation helps users understand the structure and contents of the loaded dataset.

**Available Operations:**

1. **Display First 5 Rows (`head()`)** – Displays the first five records of the dataset.
2. **Display Last 5 Rows (`tail()`)** – Displays the last five records.
3. **Display Column Names (`columns`)** – Displays all column names.
4. **Display Data Types (`dtypes`)** – Shows the data type of each column.
5. **Display Basic Info (`info()`)** – Provides information about columns, non-null values, and memory usage.
6. **Display Statistical Summary (`describe()`)** – Displays count, mean, standard deviation, minimum, maximum, and quartile values.

### 3. Perform DataFrame Operations

This section performs different operations on the loaded DataFrame.

**1. Mathematical Operations**

- Converts numerical column data into a NumPy array.
- Performs array indexing and slicing to access selected elements.
- Performs addition, subtraction, multiplication, and division on numerical data.

**2. Combine DataFrames**

- **Concatenation (`pd.concat()`)** – Combines multiple DataFrames by placing them together.
- **Merge (`merge()`)** – Combines DataFrames using a common column.
- **Join (`join()`)** – Combines DataFrames based on their indexes.

**3. Split DataFrames**

- Splits the dataset based on a selected column, such as Region or Product.
- Displays separate groups of records for each category.

**4. Search, Sort and Filter**

- **Search** – Finds records matching a selected product or condition.
- **Sort** – Arranges records in ascending or descending order.
- **Filter** – Displays only records that satisfy the given condition.

**5. Aggregate Functions**

Performs calculations on numerical columns.

- **Sum (`sum()`)** – Calculates the total value.
- **Mean (`mean()`)** – Calculates the average value.
- **Count (`count()`)** – Counts non-missing values.
- **Minimum (`min()`)** – Finds the smallest value.
- **Maximum (`max()`)** – Finds the largest value.

**6. Create Pivot Table**

- Uses `pivot_table()` to summarize sales information.
- Groups data using selected categories such as Region and Product.
- Displays summarized sales values in a tabular format.

**7. GroupBy and Transform**

- **GroupBy (`groupby()`)** – Groups records according to a selected column.
- **Transform (`transform()`)** – Performs calculations within each group and returns results aligned with the original rows.
- Helps calculate group-wise values, such as average sales for each product.

**8. Reindex and Alter Labels**

- **Reindex (`reindex()`)** – Changes the order of rows or columns according to specified labels.
- **Rename (`rename()`)** – Changes selected column names.
- Helps organize the DataFrame in the required structure.

### 4. Handle Missing Data

This operation manages missing values and improves dataset quality.

**Available Operations:**

1. **Display Rows with Missing Values (`isnull()`)** – Identifies and displays rows containing missing values.
2. **Fill Missing Values with Mean (`fillna()`)** – Replaces missing numerical values with their column mean.
3. **Drop Rows with Missing Values (`dropna()`)** – Removes rows containing missing values.
4. **Replace with a Specific Value (`fillna()`)** – Replaces missing values with a user-specified value.
5. **Remove Duplicate Records (`drop_duplicates()`)** – Removes repeated records from the dataset.
6. **Convert Data Types (`astype()`, `pd.to_datetime()`)** – Converts columns into the required data types, including date and time formats.

### 5. Generate Descriptive Statistics

This operation performs statistical analysis on numerical columns.

**Available Operations:**

1. **Descriptive Statistics (`describe()`)** – Displays count, mean, standard deviation, minimum, maximum, and quartile values.
2. **Standard Deviation (`std()`)** – Measures how much values vary from their mean.
3. **Variance (`var()`)** – Measures the spread of numerical values.
4. **Percentile (`quantile()`)** – Calculates the value at a specified quantile.

### 6. Data Visualization

This operation represents sales data graphically using Matplotlib and Seaborn.

**Available Charts:**

1. **Bar Plot** – Compares values across different categories.
2. **Line Plot** – Shows trends and changes in data.
3. **Scatter Plot** – Displays the relationship between two numerical columns.
4. **Pie Chart** – Shows the percentage or proportion of different categories.
5. **Histogram** – Displays the frequency distribution of numerical values.
6. **Stack Plot** – Shows cumulative values of different categories.
7. **Heatmap** – Displays correlations between numerical columns using colors.
8. **Box Plot** – Shows data distribution, median, quartiles, and potential outliers.
9. **Subplots** – Displays multiple charts together in a single figure.

### 7. Save Visualization

- Uses Matplotlib's `savefig()` function to save the generated chart.
- Accepts a user-defined file name.
- Saves the visualization in image format, such as PNG.

### 8. Exit

- Terminates the program when the user selects option 8.
- Displays a goodbye message.
- The destructor displays the program closing message when the object is destroyed.

---

## 📚 Concepts Used in This Project

### 1. Python Concepts

- **Class and Object:** The `SalesDataAnalyzer` class groups related operations, and its object is used to access the methods.
- **Constructor (`__init__`):** Initializes the object and its attributes.
- **Destructor (`__del__`):** Executes when the object is destroyed.
- **Methods:** Separate methods perform different data analysis operations.
- **Conditional Statements (`if-elif-else`):** Execute operations according to the user's menu selection.
- **Loops (`while`):** Repeatedly display the menu until the user exits.
- **Exception Handling (`try-except`):** Handles errors during file loading and data processing.
- **Main Function:** Organizes the execution of the program.
- **Main Guard (`if __name__ == "__main__"`):** Runs the main function when the file is executed directly.

### 2. Pandas Concepts

- **DataFrame:** Stores and manipulates sales data in rows and columns.
- **CSV File Handling:** Reads sales data using `read_csv()`.
- **Data Exploration:** Uses `head()`, `tail()`, `columns`, `dtypes`, `info()`, and `describe()`.
- **Data Selection and Filtering:** Accesses and filters selected records and columns.
- **Missing Data Handling:** Uses `isnull()`, `fillna()`, and `dropna()`.
- **Duplicate Removal:** Uses `drop_duplicates()`.
- **Data Type Conversion:** Uses `astype()` and `pd.to_datetime()`.
- **Data Combination:** Uses `concat()`, `merge()`, and `join()`.
- **Data Grouping:** Uses `groupby()` and `transform()`.
- **Aggregate Functions:** Uses `sum()`, `mean()`, `count()`, `min()`, and `max()`.
- **Pivot Table:** Uses `pivot_table()` to summarize data.
- **Reindexing and Renaming:** Uses `reindex()` and `rename()`.
- **Statistical Functions:** Uses `describe()`, `std()`, `var()`, and `quantile()`.

### 3. NumPy Concepts

- **NumPy Array:** Creates numerical arrays using `np.array()`.
- **Array Indexing:** Accesses individual elements from an array.
- **Array Slicing:** Extracts selected portions of an array.
- **Arithmetic Operations:** Performs addition, subtraction, multiplication, and division on numerical arrays.

### 4. Data Visualization Concepts

- **Matplotlib:** Used to create and display different types of charts.
- **Seaborn:** Used to create statistical visualizations such as heatmaps.
- **Bar Plot:** Compares categories.
- **Line Plot:** Displays trends.
- **Scatter Plot:** Shows relationships between numerical variables.
- **Pie Chart:** Represents proportions.
- **Histogram:** Shows frequency distribution.
- **Stack Plot:** Displays cumulative values.
- **Heatmap:** Represents numerical relationships using colors.
- **Box Plot:** Displays data distribution and potential outliers.
- **Subplots:** Displays multiple charts in one figure.
- **Save Figure:** Saves generated visualizations using `savefig()`.

---

## ▶️ How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone <repository-url>
```

**Step 2:** Open the project folder in VS Code.

```bash
cd Project-9
```

**Step 3:** Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn
```

**Step 4:** Run the Python program.

```bash
python SalesDataAnalyzer.py
```

**Step 5:** Enter the CSV dataset file path when prompted.

```text
sales_data.csv
```

**Step 6:** Select the required option from the menu and perform data analysis and visualization operations.

---

## 💻 Sample Output

### Program Initialization and Main Menu

```text
Sales Data Analyzer Initialized!

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
==========================================================

Enter your choice: 1
Enter the path of the dataset (CSV file): sales_data.csv

== Load Dataset ==
Dataset loaded successfully!
```

### Explore Data – First 5 Rows

```text
Enter your choice: 2

== Explore Data ==
1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic info
6. Display Statistical Summary

Enter your choice: 1

   SalesID    Product      Region  Sales  Profit  Quantity       Date
0      101  Product A       North  500.0   120.0       5.0  1/15/2022
1      102  Product B        East  600.0   150.0       6.0  1/20/2022
2      103  Product C  West Coast  700.0   180.0       7.0   2/5/2022
3      104  Product D       South  800.0   210.0       8.0  2/18/2022
4      105  Product E     Central  550.0   130.0       5.0   3/2/2022
```

### Aggregate Functions – Sum

```text
Enter your choice: 3

== Perform DataFrame Operations ==
1. Mathematical Operations
2. Combine DataFrames
3. Split DataFrames
4. Search, Sort and Filter
5. Aggregate Functions
6. Create Pivot Table
7. GroupBy and Transform
8. Reindex and Alter Labels

Enter your choice: 5

== Aggregate Functions ==
1. Sum
2. Mean
3. Count
4. Minimum
5. Maximum

Enter your choice: 1

Enter Numeric Column Name: Sales

Sum: 37290.0
```

### Handle Missing Data

```text
Enter your choice: 4

== Handle Missing Data ==
1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with a specific value
5. Remove Duplicate Records
6. Convert Data Types

Enter your choice: 1

    SalesID    Product      Region   Sales  Profit  Quantity       Date
36      137  Product B        East     NaN   160.0       6.0   7/5/2023
37      138  Product C     Central   850.0     NaN       8.0  7/19/2023
38      139  Product D         NaN   760.0   195.0       7.0   8/3/2023
39      140  Product E  West Coast   680.0   165.0       NaN  8/17/2023
40      141  Product A        East  1020.0   290.0      10.0        NaN
```

### Statistical Analysis – Descriptive Statistics

```text
Enter your choice: 5

== Statistical Analysis ==
1. Descriptive Statistics
2. Standard Deviation
3. Variance
4. Percentile

Enter your choice: 1

          SalesID        Sales      Profit   Quantity
count   51.000000    50.000000   50.000000  50.000000
mean   125.039216   745.800000  192.000000   7.080000
std     14.801298   149.216867   50.517728   1.523155
min    101.000000   450.000000  100.000000   4.000000
25%    112.500000   625.000000  151.250000   6.000000
50%    125.000000   730.000000  180.000000   7.000000
75%    137.500000   867.500000  233.750000   8.000000
max    150.000000  1050.000000  300.000000  10.000000
```

### Data Visualization – Histogram

```text
Enter your choice: 6

== Data Visualization ==
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Heatmap
8. Box Plot
9. Subplots

Enter your choice: 5

Histogram displayed successfully!
```

### Save Visualization

```text
Enter your choice: 7

== Save Visualization ==
Enter file name to save the plot (e.g., scatter_plot.png): product_sales.png

Visualization saved as product_sales.png successfully!
```

### Exit Program

```text
Enter your choice: 8

Exiting the program, Goodbye!

Sales Data Analyzer Closed!
```

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Work with CSV datasets using Pandas.
- Perform numerical operations using NumPy.
- Explore and manipulate DataFrames.
- Handle missing and duplicate values.
- Combine, split, group, and transform datasets.
- Apply aggregate and statistical functions.
- Create pivot tables and perform data analysis.
- Generate different types of visualizations using Matplotlib and Seaborn.
- Save generated charts as image files.
- Develop an interactive menu-driven Python application.

---

