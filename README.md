# PythonAssignment3
## My third and las assignment using Python at Cork College of Commerce.
# PROGRAM SPECIFICATION:
<br><br>
You are required to produce a Python program that calculates an employee’s tax, USC, gross and net pay as described below. The program will be modularised appropriately (i.e., will include functions). The program begins by welcoming the user and summarising what the program does.<br>
The user is then prompted to enter the employee’s id. (This must be numeric and at least 5 digits in length.) The basic hours worked this week followed by the number of overtime hours worked are then entered. The user will be re-prompted as necessary where invalid data is entered.<br><br>
The following menu is then presented:<br>
1. Calculate Gross Pay<br>
2. Calculate USC and Tax 3. Calculate Net Pay<br>
4. Summary<br>
5. Exit<br><br>
<b>Options 1-3</b> will display appropriately formatted information.<br>
<b>Option 4</b> will display a well-formatted summary to include: employee id, basic hours
worked, overtime hours worked, gross pay, USC, tax and net pay.<br><br>
After the results of any of the options 1 – 4 are displayed the menu is redisplayed. <br><br>The program exits with a suitable message when option 5 is selected.<br><br>
If an invalid menu option is entered the menu is redisplayed.<br><br>
### Note:<br>
• <b>No global variables will be used in the program.</b> (Values will be passed to functions in the arguments and results returned as appropriate.)<br>
• <b>Break and continue</b> will not be used.<br>
• Basic rate per hour is €50.43.<br>
• Overtime pay per hour is calculated as follows: the overtime rate is 1.5 x basic rate where the
basic gross pay (before tax) is less than €1700, otherwise the overtime rate is 2 x basic rate <br>
• USC is calculated using the total of the basic gross pay and the overtime pay.<br>
There is no USC for the first €250 earned per week. USC is charged at 1.5% for the next €200 and the remainder is charged at 2%<br>
• Tax is calculated using the total of the basic gross pay and the overtime pay after any USC has been deducted.<br>
The tax rate is 22.5% for the first €1200 and 40.5% for the remaining.<br><br>
The program will include at least the following functions (and may include others you deem necessary to produce a well-designed modular program):<br>
• Function to calculate and return the gross pay<br>
• Function to calculate and return the USC and tax<br>
• Function to calculate and return net pay<br>
• Function (s) to display output<br>
