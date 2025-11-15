# BANK-MANAGEMENT-SYSTEM

### OVERVIEW
This project is a simple console-based application that helps manage basic banking operations. It uses Python for handling the application logic and MySQL as the backend database for storing customer and account details. The system allows users to create accounts, view account details, deposit and withdraw money, check balances, and manage transaction records. It provides a structured and secure way to organize banking data and demonstrates the integration of Python with MySQL for real-world database operations.
<img width="1900" height="767" alt="output" src="https://github.com/user-attachments/assets/cd33dbbc-b15e-4fbd-b567-2ad83d99cd84" />
<img width="1902" height="687" alt="output_contn" src="https://github.com/user-attachments/assets/21e45fe9-91a4-4b73-bfc9-e9cbdf6190ff" />

### TOOL REQUIREMENT

1. Python – To build the application logic<br>
2. MySQL Workbench – To store and manage account data<br>
3. VS Code – Code editor for development

### Description – account_operations.py
1. create_account()
This function is responsible for creating a new bank account. It collects the customer's name, email, and opening balance from user input, connects to the database, and inserts a new record into the accounts table. Once the operation is committed successfully, it confirms account creation and closes the database connection.

2. view_accounts()
The purpose of this function is to retrieve and display all existing accounts stored in the database. It executes a SELECT query on the accounts table, fetches all results, and prints each account’s ID, name, email, and current balance in a clear format. Finally, it closes the database connection.

3. deposit_money()
This function handles the deposit process. After receiving the account ID and deposit amount from the user, it updates the corresponding account by adding the specified amount to the existing balance. The updated information is committed to the database, and a confirmation message is displayed.

4. withdraw_money()
This function manages withdrawal operations. It first checks the current balance of the provided account ID. If sufficient funds are available, it deducts the withdrawal amount and updates the balance accordingly. If the balance is inadequate, it displays an appropriate error message. The database connection is then closed.

5. check_balance()
This function allows the user to view the balance of a specific account. It retrieves the account holder’s name and current balance using the given account ID. If the account exists, the details are displayed; otherwise, an error message indicates that the account was not found.
   

