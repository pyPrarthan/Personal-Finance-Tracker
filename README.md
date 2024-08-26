# 💰 Personal Finance Tracker

This Python project, inspired by [this YouTube video](https://www.youtube.com/watch?v=Dn1EjhcQk64), is designed to help you manage and track your personal finances. It allows you to record income and expenses, view transactions within a specific date range, and visualize your financial data with a simple plot.

## 📂 Project Structure

- `main.py`: The main script for running the finance tracker. Includes features for adding transactions, viewing summaries, and plotting data.
- `data_entry.py`: Contains helper functions for input and validation, such as date, amount, category, and description.
- `finance_data.csv`: CSV file where your financial transactions are stored. Automatically created if it doesn't exist.

## 🚀 Features

1. **Add New Transactions**: Record income or expenses with details like date, amount, category, and description.
2. **View Transactions**: Filter and view transactions within a specified date range.
3. **Summary**: Get a summary of total income, total expenses, and net savings.
4. **Visualization**: Generate a plot to visualize income and expenses over time.

## 🛠️ How to Use

1. **Initialize CSV File**: The program automatically creates a `finance_data.csv` file if it doesn't already exist.
2. **Add a Transaction**: Run the script and select the option to add a new transaction. Enter the required details such as date, amount, category, and description.
3. **View Transactions**: Choose the option to view transactions and specify the date range. View a summary of your financial activity.
4. **Plot Data**: Optionally, generate a plot to visualize your financial data over time.

## 📊 Example Usage

```python
# To add a new transaction
CSV.add_entry("26-08-2024", 150.00, "Income", "Freelance Work")

# To view and summarize transactions within a date range
CSV.get_transaction("01-08-2024", "31-08-2024")
```python

## 📈 Visualization

The project includes basic data visualization. Use the plot feature to see your income and expenses over time. This helps you gain insights into your financial trends and patterns.

## 🧩 Requirements
- Python
- Pandas
- Matplotlib
