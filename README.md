# Python CLI Wallet App 
Simple Wallet application using Python OOP

1. Class `Wallet` can be used to create a simple wallet object (as shown in driver code).
- Perform simple wallet operations such as tracking expenses (ledger), withdrawal/deposit money, transfer money etc.
- Using the Wallet.read_from_csv() method, parse CSV files containing transaction information


2. CSV file format:

Columns : Type, Amount, Category, Description


Type = ['W', 'D', 'T', 'S', 'R']

- W: Withdraw
- D: Deposit
- T: Transfer
- S: Spend/Swipe
- R: Receive


3. Log all transactions in the above format in a csv file and store in root folder. 

Example:

Type, Amount, Category, Description <br>
'D', 2000, Salary, '' <br>
'W', 500, '', '' <br> 
'T', 100, '', 'Tom' <br> 
'S', 50, 'Food', 'Burger' <br> 
'S', 100, 'Clothing', 'Jeans' <br>

<br>

Sample Output: <br>
>> python driver.py
>> Wallet: 'Sample' created!
>> 2000 deposited
>> 500 withdrawn
>> 100 transferred to Tom
>> 50 spent on Food: Burger
>> 100 spent on Clothing: Jeans
>> 500 received from Harry
