# Function for welcoming user
def welcomingUser():
    print("***"*26)
    print("Hello. This program will calculates an employee`s Tax, USC, Gross and Net Pay.")
    print("***" * 26)


# Function for asking to enter how many hours user worked
def askUsersData():
    userID = "id"  # Variable for users ID
    basicsHours = "hours"  # Variable for worked basics hours
    overTimeHours = "hours"  # Variable for worked over time hours
    while len(userID) < 5 or not userID.isdigit():  # While loop which working until user entered a correct ID
        userID = input("\nEnter your ID: ")
        if len(userID) < 5 or userID.isdigit() == False:
            print("Sorry, your ID must be numeric and at least 5 digits in length.")  # Saying to user that he did
            # mistake
    while not basicsHours.isdigit():  # While loop which working until user entered a correct basic hours
        basicsHours = input("\nEnter how many basic hours you did: ")
        if not basicsHours.isdigit():
            print("Sorry, use only digits.")  # Saying to user that he did
    while not overTimeHours.isdigit():
        overTimeHours = input("\nEnter how many overtime hours you did: ") # While loop which working until user entered
        # a correct over time hours
        if not overTimeHours.isdigit():
            print("Sorry, use only digits.")  # Saying to user that he did
    return userID, basicsHours, overTimeHours  # Return a users ID, how many basic and over time hours worked


# Function which calculating a gross pay
def calculateGrossPay(basicsHours, overTimeHours):
    basicPay = int(basicsHours)*50.43  # Calculating a basic pay
    if basicPay < 1700:
        grossPay = basicPay+int(overTimeHours)+(50.43*1.5)  # Calculating a gross pay
    else:
        grossPay = basicPay+int(overTimeHours)*(50.43*2)    # Calculating a gross pay
    return grossPay  # Return a gross pay


# Function which calculating a Tax and USC
def calculateUSCTax(grossPay):
    if grossPay < 250:
        usc = 0
    elif grossPay < 450:
        usc = ((grossPay-250)*(1.5/100))  # Calculating a USC
    else:
        usc = (((grossPay-450)*(2/100))+((200*1.5)/100))
    # Calculating tax after paid USC
    if grossPay-usc < 1200:
        tax = (grossPay-usc)*22.5/100  # Calculating a Tax
    else:
        tax = ((grossPay - usc-1200) * 40.5 / 100 + 1200*22.5/100)
    return tax, usc  # Return a USC and Tax


# Function which calculating a Net pay
def calculateNetPay(grossPay, usc, tax):
    netPay = grossPay-usc-tax  # Calculating Net pay
    return netPay  # Return Net pay


# Function which have to output menu
def menu(grossPay, usc, tax, netPay, userID, basicsHours, overTimeHours):
    again = True  # Variable to show menu again or not
    while again:  # While loop which working until user entered a number 5
        print("\n")
        print("***" * 10)
        print("Choose what you want to do:")
        print("***" * 10)
        # Output a menu
        print("1. Calculate Gross Pay\n2. Calculate USC and Tax\n3. Calculate Net Pay\n4. View Summary\n5. Exit")
        print("***" * 10)
        option = ""
        # While loop which working until user entered a correct number from 1 to 5
        while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" or not option.isdigit():
            option = input("\nPlease, enter a number of option: ")
            if option != "1" and option != "2" and option != "3" and option != "4" and option != "5"  or option.isdigit() == False:
                print("Sorry, enter a number between 1 and 5.")
        # If statement for each choice of User
        if option == "1":
            print("\n")
            print("***" * 10)
            print("Statement for User ID: ", userID)
            print("***" * 10)
            print("Gross pay: ", '{:>8}'.format(""), '€{:,.2f}'.format(grossPay))
            print("***" * 10)
        if option == "2":
            print("\n")
            print("***" * 10)
            print("Statement for User ID: ", userID)
            print("***" * 10)
            print("Your USC: ", '{:>11}'.format(""), '€{:,.2f}'.format(usc))
            print("Your TAX: ", '{:>11}'.format(""), '€{:,.2f}'.format(tax))
            print("***" * 10)
        if option == "3":
            print("\n")
            print("***" * 10)
            print("Statement for User ID: ", userID)
            print("***" * 10)
            print("Your Net Pay: ", '{:>5}'.format(""), '€{:,.2f}'.format(netPay))
            print("***" * 10)
        if option == "4":
            print("\n")
            print("***" * 10)
            print("Statement for User ID: ", userID)
            print("***" * 10)
            print("Basic hours worked: ", '{:>4}'.format(""), basicsHours)
            print("Over time hours worked: ", '{:>0}'.format(""), overTimeHours)
            print("Gross pay: ", '{:>8}'.format(""), '€{:,.2f}'.format(grossPay, 2))
            print("Your USC: ", '{:>11}'.format(""), '€{:,.2f}'.format(usc))
            print("Your TAX: ", '{:>12}'.format(""), '€{:,.2f}'.format(tax))
            print("Your Net Pay: ", '{:>5}'.format(""), '€{:,.2f}'.format(netPay))
            print("***" * 10)
        if option == "5":
            print("\n")
            print("***" * 10)
            print("Thank you, good bye!")
            print("***" * 10)
            again = False


# Main function which running every function
def main():
     welcomingUser()
     id, basichour, over = askUsersData()
     gross = calculateGrossPay(basichour, over)
     usc, Tax = calculateUSCTax(gross)
     net = calculateNetPay(gross, usc, Tax)
     menu(gross, usc, Tax, net, id, basichour, over)


# Call a main function
main()