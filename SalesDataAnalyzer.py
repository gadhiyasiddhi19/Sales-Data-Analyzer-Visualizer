import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    # Constructor
    def __init__(self):
        self.data = None
        self.current_plot = None
        print("\nSales Data Analyzer Initialized!")

    # Destructor
    def __del__(self):
        print("\nSales Data Analyzer Closed!")

    # Load Dataset
    def load_data(self, file_path):
        print("\n== Load Dataset ==")
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")

        except FileNotFoundError:
            print("\nError: CSV file not found!")

        except Exception as e:
            print("\nError:", e)

    # Explore Dataset
    def explore_data(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        print("6. Display Statistical Summary")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            print(self.data.head())

        elif choice == '2':
            print(self.data.tail())

        elif choice == '3':
            print(self.data.columns)

        elif choice == '4':
            print(self.data.dtypes)

        elif choice == '5':
            self.data.info()

        elif choice == '6':
            print(self.data.describe())

        else:
            print("\nInvalid choice!")

    # Clean Dataset
    def clean_data(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        print("5. Remove Duplicate Records")
        print("6. Convert Data Types")

        choice = input("\nEnter your choice: ")

        if choice == '1':

            missing_data = self.data[self.data.isnull().any(axis=1)]

            if missing_data.empty:
                print("\nNo missing values found in the dataset!")
            else:
                print(missing_data)

        elif choice == '2':

            self.data.fillna(
                self.data.mean(numeric_only=True),
                inplace=True
            )

            print("\nMissing values filled with mean successfully!")

        elif choice == '3':

            self.data.dropna(inplace=True)

            print("\nRows with missing values dropped successfully!")

        elif choice == '4':

            value = input("\nEnter a specific value: ")
            self.data.fillna(value, inplace=True)

            print("\nMissing values replaced successfully!")

        elif choice == '5':

            self.data.drop_duplicates(inplace=True)

            print("\nDuplicate records removed successfully!")

        elif choice == '6':

            self.data['Date'] = pd.to_datetime(
                self.data['Date'],
                errors='coerce'
            )

            print("\nData types converted successfully!")
            print(self.data.dtypes)

        else:
            print("\nInvalid choice!")

    # Mathematical Operations and NumPy Arrays
    def mathematical_operations(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Mathematical Operations ==")

        print("1. Create NumPy Array")
        print("2. Display Array Indexing")
        print("3. Display Array Slicing")
        print("4. Addition")
        print("5. Subtraction")
        print("6. Multiplication")
        print("7. Division")

        choice = input("\nEnter your choice: ")

        if choice in ['1', '2', '3']:

            arr = np.array(self.data['Sales'].dropna())

            if choice == '1':
                print("\nNumPy Array:")
                print(arr)

            elif choice == '2':
                print("\nFirst Element:", arr[0])
                print("Third Element:", arr[2])

            elif choice == '3':
                print("\nFirst Five Elements:")
                print(arr[0:5])

        elif choice in ['4', '5', '6', '7']:

            value = float(input("\nEnter a number: "))

            if choice == '4':
                print(self.data['Sales'] + value)

            elif choice == '5':
                print(self.data['Sales'] - value)

            elif choice == '6':
                print(self.data['Sales'] * value)

            elif choice == '7':
                print(self.data['Sales'] / value)

        else:
            print("\nInvalid choice!")

    # Combine DataFrames
    def combine_data(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Combine DataFrames ==")

        file_path = input("\nEnter another CSV file path: ")

        try:
            other_data = pd.read_csv(file_path)

            print("1. Concatenate DataFrames")
            print("2. Merge DataFrames")
            print("3. Join DataFrames")

            choice = input("\nEnter your choice: ")

            if choice == '1':

                combined_data = pd.concat(
                    [self.data, other_data],
                    ignore_index=True
                )

                print("\nConcatenated DataFrame:")
                print(combined_data)

            elif choice == '2':

                combined_data = pd.merge(
                    self.data,
                    other_data,
                    on='SalesID'
                )

                print("\nMerged DataFrame:")
                print(combined_data)

            elif choice == '3':

                combined_data = self.data.set_index('SalesID').join(
                    other_data.set_index('SalesID'),
                    rsuffix='_other'
                )

                print("\nJoined DataFrame:")
                print(combined_data)

            else:
                print("\nInvalid choice!")

        except FileNotFoundError:
            print("\nCSV file not found!")

        except Exception as e:
            print("\nError:", e)

    # Split DataFrame
    def split_data(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Split DataFrame ==")

        print("1. Split By Region")
        print("2. Split By Product")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            column = 'Region'

        elif choice == '2':
            column = 'Product'

        else:
            print("\nInvalid choice!")
            return

        for value in self.data[column].dropna().unique():

            split_data = self.data[
                self.data[column] == value
            ]

            print("\n", column, ":", value)
            print(split_data)

    # Search, Sort and Filter
    def search_sort_filter(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Search, Sort and Filter ==")

        print("1. Search Records")
        print("2. Sort Data")
        print("3. Filter Data")

        choice = input("\nEnter your choice: ")

        if choice == '1':

            value = input("\nEnter Product Name to Search: ")

            result = self.data[
                self.data['Product'] == value
            ]

            print(result)

        elif choice == '2':

            column = input("\nEnter Column Name to Sort: ")

            if column in self.data.columns:

                result = self.data.sort_values(by=column)
                print(result)

            else:
                print("\nInvalid column name!")

        elif choice == '3':

            column = input("\nEnter Column Name: ")
            value = input("\nEnter Value to Filter: ")

            if column in self.data.columns:

                result = self.data[
                    self.data[column].astype(str) == value
                ]

                print(result)

            else:
                print("\nInvalid column name!")

        else:
            print("\nInvalid choice!")

    # Aggregate Functions
    def aggregate_functions(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Aggregate Functions ==")

        print("1. Sum")
        print("2. Mean")
        print("3. Count")
        print("4. Minimum")
        print("5. Maximum")

        choice = input("\nEnter your choice: ")

        column = input("\nEnter Numeric Column Name: ")

        if column not in self.data.columns:
            print("\nInvalid column name!")
            return

        if choice == '1':
            print("\nSum:", self.data[column].sum())

        elif choice == '2':
            print("\nMean:", self.data[column].mean())

        elif choice == '3':
            print("\nCount:", self.data[column].count())

        elif choice == '4':
            print("\nMinimum:", self.data[column].min())

        elif choice == '5':
            print("\nMaximum:", self.data[column].max())

        else:
            print("\nInvalid choice!")

    # Statistical Analysis
    def statistical_analysis(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Statistical Analysis ==")
        print("1. Descriptive Statistics")
        print("2. Standard Deviation")
        print("3. Variance")
        print("4. Percentile")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            print(self.data.describe())

        elif choice in ['2', '3', '4']:

            column = input("\nEnter Numeric Column Name: ")

            if column not in self.data.columns:
                print("\nInvalid column name!")
                return

            if choice == '2':
                print("\nStandard Deviation:")
                print(self.data[column].std())

            elif choice == '3':
                print("\nVariance:")
                print(self.data[column].var())

            elif choice == '4':

                print("\nPercentile:")
                print(self.data[column].quantile())

        else:
            print("\nInvalid choice!")

    # Create Pivot Table
    def create_pivot_table(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Create Pivot Table ==")

        pivot = pd.pivot_table(
            self.data,
            values='Sales',
            index='Region',
            columns='Product',
            aggfunc='sum'
        )

        print(pivot)

    # GroupBy and Transform
    def groupby_transform(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== GroupBy and Transform ==")
        print("1. Group By Region")
        print("2. Group By Product")
        print("3. Transform Sales Data")

        choice = input("\nEnter your choice: ")

        if choice == '1':

            result = self.data.groupby('Region')['Sales'].sum()
            print(result)

        elif choice == '2':

            result = self.data.groupby('Product')['Sales'].sum()
            print(result)

        elif choice == '3':

            self.data['Sales_Transform'] = self.data.groupby(
                'Product'
            )['Sales'].transform('mean')

            print(self.data[['Product', 'Sales', 'Sales_Transform']])

        else:
            print("\nInvalid choice!")

    # Reindex and Alter Labels
    def reindex_data(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Reindex and Alter Labels ==")
        print("1. Reindex DataFrame")
        print("2. Rename Column Labels")

        choice = input("\nEnter your choice: ")

        if choice == '1':

            result = self.data.reindex(
                columns=[
                    'SalesID',
                    'Product',
                    'Region',
                    'Sales',
                    'Profit',
                    'Quantity',
                    'Date'
                ]
            )

            print(result)

        elif choice == '2':

            print("\nAvailable Columns:")
            print(self.data.columns)

            old_name = input("\nEnter Existing Column Name: ")
            new_name = input("\nEnter New Column Name: ")

            if old_name in self.data.columns:

                self.data.rename(
                    columns={old_name: new_name},
                    inplace=True
                )

                print("\nColumn label changed successfully!")
                print(self.data.columns)

            else:
                print("\nInvalid column name!")

        else:
            print("\nInvalid choice!")

    # Data Visualization
    def visualize_data(self):

        if self.data is None:
            print("\nPlease load the dataset first!")
            return

        print("\n== Data Visualization ==")

        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Heatmap")
        print("8. Box Plot")
        print("9. Subplots")

        choice = input("\nEnter your choice: ")

        self.current_plot = None

        if choice == '1':

            result = self.data.groupby('Product')['Sales'].sum()
            self.current_plot = plt.figure()

            plt.bar(result.index, result.values)
            plt.title("Product Wise Sales")
            plt.xlabel("Product")
            plt.ylabel("Sales")

            plt.show()

        elif choice == '2':

            result = self.data.groupby('Date')['Sales'].sum() if 'Date' in self.data.columns else self.data.groupby('Year')['Sales'].sum()
            self.current_plot = plt.figure()

            plt.plot(result.index, result.values, marker='o')
            plt.title("Sales Trend")
            plt.xlabel("Date/Year")
            plt.ylabel("Sales")
            plt.xticks(rotation=45)
            plt.tight_layout()

            plt.show()

        elif choice == '3':

            print("\n== Scatter Plot ==")
            x = input("Enter x-axis column name: ")
            y = input("Enter y-axis column name: ")

            if x not in self.data.columns or y not in self.data.columns:
                print("\nInvalid column name!")
                return

            print("Generating scatter plot...")
            self.current_plot = plt.figure()

            plt.scatter(self.data[x], self.data[y])
            plt.title("Scatter Plot")
            plt.xlabel(x)
            plt.ylabel(y)
            print("Scatter plot displayed successfully!")

            plt.show()

        elif choice == '4':

            result = self.data.groupby('Product')['Sales'].sum()
            self.current_plot = plt.figure()

            plt.pie(
                result.values,
                labels=result.index,
                autopct='%1.1f%%'
            )
            plt.title("Product Wise Sales")
            plt.show()

        elif choice == '5':

            self.current_plot = plt.figure()

            plt.hist(self.data['Sales'].dropna(), bins=10)
            plt.title("Sales Distribution")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")
            print("Histogram displayed successfully!")
            plt.show()

        elif choice == '6':

            result = self.data.pivot_table(
                values='Sales',
                index='Date' if 'Date' in self.data.columns else 'Year',
                columns='Product',
                aggfunc='sum'
            )

            self.current_plot = plt.figure()

            plt.stackplot(
                result.index,
                result.fillna(0).T,
                labels=result.columns
            )

            plt.title("Product Sales Stack Plot")
            plt.xlabel("Date/Year")
            plt.ylabel("Sales")
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()

            print("Stack plot displayed successfully!")
            plt.show()

        elif choice == '7':

            result = self.data.select_dtypes(include=np.number)
            self.current_plot = plt.figure()
            sns.heatmap(result.corr(), annot=True)
            plt.title("Sales Data Heatmap")
            plt.show()

        elif choice == '8':

            self.current_plot = plt.figure()
            sns.boxplot(
                data=self.data,
                x='Product',
                y='Sales'
            )
            plt.title("Product Sales Box Plot")
            plt.show()

        elif choice == '9':

            self.current_plot, axes = plt.subplots(2, 2)

            axes[0, 0].bar(
                self.data['Product'],
                self.data['Sales']
            )
            axes[0, 0].set_title("Bar Plot")

            axes[0, 1].plot(self.data['Sales'])
            axes[0, 1].set_title("Line Plot")

            axes[1, 0].scatter(
                self.data['Sales'],
                self.data['Profit'] if 'Profit' in self.data.columns else self.data['Sales']
            )
            axes[1, 0].set_title("Scatter Plot")

            axes[1, 1].hist(
                self.data['Sales'].dropna(),
                bins=10
            )
            axes[1, 1].set_title("Histogram")

            plt.tight_layout()
            plt.show()

        else:
            print("\nInvalid choice!")

    # Save Visualization
    def save_visualization(self):

        if self.current_plot is None:
            print("\nPlease generate a visualization first!")
            return

        print("\n== Save Visualization ==")
        file_name = input(
            "Enter file name to save the plot (e.g., scatter_plot.png): "
        )

        self.current_plot.savefig(file_name)

        print("Visualization saved as", file_name, "successfully!")


# Main Function
def main():

    analyzer = SalesDataAnalyzer()

    while True:

        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")

        print("==========================================================")

        choice = input("\nEnter your choice: ")

        if choice == '1':

            file_path = input(
                "Enter the path of the dataset (CSV file): "
            )

            analyzer.load_data(file_path)

        elif choice == '2':

            analyzer.explore_data()

        elif choice == '3':

            if analyzer.data is None:
                print("\nPlease load the dataset first!")
                continue

            print("\n== Perform DataFrame Operations ==")

            print("1. Mathematical Operations")
            print("2. Combine DataFrames")
            print("3. Split DataFrames")
            print("4. Search, Sort and Filter")
            print("5. Aggregate Functions")
            print("6. Create Pivot Table")
            print("7. GroupBy and Transform")
            print("8. Reindex and Alter Labels")

            sub_choice = input("\nEnter your choice: ")

            if sub_choice == '1':
                analyzer.mathematical_operations()

            elif sub_choice == '2':
                analyzer.combine_data()

            elif sub_choice == '3':
                analyzer.split_data()

            elif sub_choice == '4':
                analyzer.search_sort_filter()

            elif sub_choice == '5':
                analyzer.aggregate_functions()

            elif sub_choice == '6':
                analyzer.create_pivot_table()

            elif sub_choice == '7':
                analyzer.groupby_transform()

            elif sub_choice == '8':
                analyzer.reindex_data()

            else:
                print("\nInvalid choice!")

        elif choice == '4':
            analyzer.clean_data()

        elif choice == '5':
            analyzer.statistical_analysis()

        elif choice == '6':
            analyzer.visualize_data()

        elif choice == '7':
            analyzer.save_visualization()

        elif choice == '8':
            print("\nExiting the program, Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Main Program
if __name__ == "__main__":
    main()