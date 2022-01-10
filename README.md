# Python CLI Wallet App 

Simple Wallet application using Python OOP

Takes .csv files as input and displays summary of transactions

CSV file format:

Columns : Type, Amount, Category, Description


Type = ['W', 'D', 'T', 'S', 'R']

W: Withdraw
D: Deposit
T: Transfer
S: Spend/Swipe
R: Receive


Log all transactions using the above format and store in root folder. 
Example:

Type, Amount, Category, Description
'D', 2000, Salary, '' \n
'W', 500, '', '' \n
'T', 100, '', 'Tom' \n
'S', 50, 'Food', 'Burger' \n
'S', 100, 'Clothing', 'Jeans' \n
