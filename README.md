# 💰 Personal Finance Tracker with FinBot 🤖

This Python project, is designed to help you manage and track your personal finances. It allows you to record income and expenses, view transactions within a specific date range, and visualize your financial data with a simple plot.

## 📂 Project Structure

- `main.py`: The main script for running the finance tracker. Includes features for adding transactions, viewing summaries, and plotting data.
- `data_entry.py`: Contains helper functions for input and validation, such as date, amount, category, and description.
- `finance_data.csv`: CSV file where your financial transactions are stored. Automatically created if it doesn't exist.
- `finBot.py`: Script that powers FinBot, an AI-driven chatbot that provides financial advice. It handles the interaction between the user and OpenAI's GPT model to answer questions related to budgeting, saving, and other finance-related queries.


## 🚀 Features

1. **Add New Transactions**: Record income or expenses with details like date, amount, category, and description.
2. **View Transactions**: Filter and view transactions within a specified date range.
3. **Summary**: Get a summary of total income, total expenses, and net savings.
4. **Visualization**: Generate a plot to visualize income and expenses over time.
5. **FinBot**: Chat with a Bot if you need any financial aid.

## 🦾 FinBot Features:

1. Financial Advice: Ask **FinBot** questions like **"How can I save more money?"** or **"What should I know about budgeting?"** for helpful insights.
2. Interactive Chat: Chat with FinBot directly through the terminal to get quick financial tips.
3. Seamless Integration: FinBot is integrated into the existing Personal Finance Tracker, making it a one-stop solution for managing and understanding your finances.
4. Type 'exit' to return to main menu. 

## 🛠️ How to Use

1. **Initialize CSV File**: The program automatically creates a `finance_data.csv` file if it doesn't already exist.
2. **Add a Transaction**: Run the script and select the option to add a new transaction. Enter the required details such as date, amount, category, and description.
3. **View Transactions**: Choose the option to view transactions and specify the date range. View a summary of your financial activity.
4. **Plot Data**: Optionally, generate a plot to visualize your financial data over time.
5. **Fin Bot**: You can simply ask the Bot questions which uses gpt-3.5-turbo model. 

## 📈 Visualization

The project includes basic data visualization. Use the plot feature to see your income and expenses over time. This helps you gain insights into your financial trends and patterns.

## 🧩 Requirements
- Python
- Pandas
- Matplotlib

