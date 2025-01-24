
#function dump
#Universal login functions
from datetime import datetime
cusdat = "Customer_Data.txt"
stfdat = "Staff_Data.txt"
admdat = "Admin_Data.txt"
supdat = "Super_User_Data.txt"
def user_count(USER_DATA):
    with open(USER_DATA, 'r') as fp:
        user_counter = sum(1 for line in fp)
        return user_counter
def customer_database():
    allUsers = []
    with open("Customer_Data.txt") as fh:
        for rec in fh:
            allUsers.append(rec.strip().split(" "))
    return allUsers
def staff_database():
    allUsers = []
    with open("Staff_Data.txt") as fh:
        for rec in fh:
            allUsers.append(rec.strip().split(" "))
    return allUsers
def admin_database():
    allUsers = []
    with open("Admin_Data.txt") as fh:
        for rec in fh:
            allUsers.append(rec.strip().split(" "))
    return allUsers
def SuperUser_database():
    allUsers = []
    with open("Super_User_Data.txt") as fh:
        for rec in fh:
            allUsers.append(rec.strip().split(" "))
    return allUsers
def validate_int(input_value):
    try:
        input_value = int(input_value)
        return True
    except ValueError:
        return False
def double_validation(error_message):
   #assumes user had already input a wrong answer
    while True:
        print("Invalid input, please enter 1 to try again") #can be put into parameter to display specific error message
        choice = input("Please enter option: ")
        if choice in "1":
            print(error_message)
            break
def increment_id(user_id,USER_DATA):
    letters = user_id[0:6]
    numbers = int(user_id[6:])
    new_num = numbers + user_count(USER_DATA)
    usrnum = str("{:04d}".format(new_num))
    final_user_id = letters + usrnum
    return final_user_id
def get_existing_users(USER_DATA):
    with open(USER_DATA,"r") as fp:
        content = fp.readlines()
        for line in content:
            print(line.split()[1])
def ask_user_credentials():
    print("Please Enter Login Details:")
    name = str(input("User_ID: "))
    password = str(input("Password: "))
    return name, password
#transaction function dump
def add_new_transaction(transaction_history, date, time, transaction_type, amount):
    new_transaction = f'{date},{time},{transaction_type},{amount}\n'
    #transaction_history.append(new_transaction)
    return new_transaction
def save_transaction_history(transaction_history, file_name):
    with open(file_name, 'a') as file:
        file.writelines(transaction_history)
def load_transaction_history(file_name):
    transaction_history = []
    with open(file_name, "r") as file:
        for line in file:
            transaction_history.append(line.strip())
    return transaction_history



def get_current_time():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime('%Y-%m-%d')
    formatted_time = current_datetime.strftime('%H:%M')
    return formatted_time, formatted_date
def is_date_in_range(date, start_date, end_date):
    #date = datetime.strptime(date,"%Y-%m-%d")
    return start_date <= date <= end_date
def filter_transactions_by_date(transactions, start_date, end_date):
    filtered_transactions = [date for date in transactions if is_date_in_range(date[0], start_date, end_date)]
    return filtered_transactions
# Print the loaded transaction history data
def print_history(filtered_transactions):
    for transaction in filtered_transactions:
        print(transaction)

def customer_registration_input():
    print("Please Provide New Customer Details: ")
    zloop = 1
    while zloop == 1:
        rawname = str(input("Name: "))
        name = rawname.replace(' ', '-')
        while True:
            password = str(input("Password: "))
            if len(password) >= 8:
                break
            else:
                double_validation("Password must be atleast 8 digits")

        while True:
            balancestr = (input("Starting balance: "))
            if validate_int(balancestr) == True and int(balancestr) >= 1000:
                balance = balancestr
                break
            else:
                double_validation("Minimum input balance is 1000, Please deposit an amount greater than the minimum")

        occupation = str(input("Occupation: "))

        while True:
            gender = str(input("Gender (M or F only): ")).upper()  # M OR F
            if gender in ['F', 'M']:
                wloop = 1
                break
            else:
                double_validation("Invalid input, Please enter either M or F")
        while True:
            citystr = (input("City.no (From 1-9 only): "))
            if validate_int(citystr) == True and 1 <= int(citystr) <= 9:
                city = '0' + str(citystr)
                break
            else:
                double_validation("Input Invalid, Please enter a number from 1-9")
        while True:
            branchstr = (input("Branch.no (From 1-9 only): "))
            if validate_int(branchstr) == True and 1 <= int(branchstr) <= 9:
                branch = '0' + str(branchstr)
                break
            else:
                double_validation("Input Invalid, Please enter a number from 1-9")
        while True:
            acc_type = str(input("Current or saving (C or S): ").upper())  # in C or S
            if acc_type in ['C', 'S']:
                break
            else:
                double_validation("Invalid account type, Please enter either C or S ONLY")
        while True:
            email = input("Email Address: ")
            if '@' in email and '.' in email:
                break
            else:
                double_validation("Please enter you email in a proper format(user@mail.com)")
        print("Please enter your birthdate in a double digit format (e.g 29/01/2000): \n")  # general date validation
        while True:
            year_str = (input("Year: "))
            if validate_int(year_str)== True and int(year_str) >= 1900 and int(year_str) <= 2005:
                year = int(year_str)
                break
            else:
                double_validation("Year is not eligible in our criteria, Please enter a year between 1900 and 2005")

        while True:
            month_str = (input("Month: "))
            if validate_int(month_str) == True and int(month_str) >= 1 and int(month_str) <= 12:
                month = int(month_str)
                break
            else:
                double_validation("You may have entered the month incorrectly, Please enter a month between 1-12")

        while True:
            day_str = (input("Day: "))
            if validate_int(day_str) == True and int(day_str) >= 1 and int(day_str) <= 31:
                day = int(day_str)
                break
            else:
                double_validation("You may have entered the day incorrectly, Please enter a day between 1-31")
        rawbirthdate = datetime(year, month, day)
        birthdate = rawbirthdate.strftime('%Y-%m-%d')
        rawregistration_time = datetime.now()
        registration_time = rawregistration_time.strftime('%Y-%m-%d')
        print(f"Customer Details: \nName = {name}\nPassword = {password}\nStarting Balance = {balance}\nOccupation = {occupation}\nGender = {gender}\nCity code = {city}\nBranch code = {branch}\nAccount type = {acc_type}\nEmail Address = {email}\nDate of birth = {birthdate}\n")
        zloop = int(input("Please Double check the entered details: \nID and Name are final and unchangable\nif you would like to proceed, press 0\nif you would like to re-enter the details, press 1\n"))
        if zloop == 0:
            return name, password, balance, occupation, gender, city, branch, acc_type, email, birthdate, registration_time


def register_customer():
    name, password, balance, occupation, gender, city, branch, acc_type, email, birthdate, registration_time = customer_registration_input()
    base_user_id = "C" + acc_type + city + branch + "0001"
    final_user_id = increment_id(base_user_id, cusdat)
    acc_history = " "
    data = ""
    with open(f"{final_user_id}_history.txt", 'w') as file:
        file.write(data)
    with open(cusdat, "a") as fp:
        fp.write(f"{final_user_id} {name} {password} {balance} {occupation} {gender} {city} {branch} {acc_type} {email} {birthdate} {registration_time} {acc_history} \n")
    print(f"User registered successfully\n User ID is {final_user_id}")
    return True
#Staff exclusive functions:
def staff_registration_input():
    print("Please Provide New Staff Details: ")
    zloop = 1
    while zloop == 1:
        rawname = str(input("Name: "))
        name = rawname.replace(' ', '-')
        while True:
            balancestr = (input("Starting balance: "))
            if validate_int(balancestr) == True and int(balancestr) >= 1000:
                balance = balancestr
                break
            else:
                double_validation("Minimum input balance is 1000, Please deposit an amount greater than the minimum")

        occupation = "Staff"

        while True:
            gender = str(input("Gender (M or F only): ")).upper()  # M OR F
            if gender in ['F', 'M']:
                wloop = 1
                break
            else:
                double_validation("Invalid input, Please enter either M or F")
        while True:
            citystr = (input("City.no (From 1-9 only): "))
            if validate_int(citystr) == True and 1 <= int(citystr) <= 9:
                city = '0' + str(citystr)
                break
            else:
                double_validation("Input Invalid, Please enter a number from 1-9")
        while True:
            branchstr = (input("Branch.no (From 1-9 only): "))
            if validate_int(branchstr) == True and 1 <= int(branchstr) <= 9:
                branch = '0' + str(branchstr)
                break
            else:
                double_validation("Input Invalid, Please enter a number from 1-9")
        while True:
            acc_type = str(input("Current or saving (C or S): ").upper())  # in C or S
            if acc_type in ['C', 'S']:
                break
            else:
                double_validation("Invalid account type, Please enter either C or S ONLY")
        print("Please enter your birthdate in a double digit format (e.g 29/01/2000): \n")  # general date validation
        while True:
            year_str = (input("Year: "))
            if validate_int(year_str)== True and int(year_str) >= 1900 and int(year_str) <= 2005:
                year = int(year_str)
                break
            else:
                double_validation("Year is not eligible in our criteria, Please enter a year between 1900 and 2005")

        while True:
            month_str = (input("Month: "))
            if validate_int(month_str) == True and int(month_str) >= 1 and int(month_str) <= 12:
                month = int(month_str)
                break
            else:
                double_validation("You may have entered the month incorrectly, Please enter a month between 1-12")

        while True:
            day_str = (input("Day: "))
            if validate_int(day_str) == True and int(day_str) >= 1 and int(day_str) <= 31:
                day = int(day_str)
                break
            else:
                double_validation("You may have entered the day incorrectly, Please enter a day between 1-31")
        rawbirthdate = datetime(year, month, day)
        birthdate = rawbirthdate.strftime('%Y-%m-%d')
        rawregistration_time = datetime.now()
        registration_time = rawregistration_time.strftime('%Y-%m-%d')
        password = "blank"
        email = "blank"
        print(f"Staff Details: \nName = {name}\nStarting Balance = {balance}\nOccupation = {occupation}\nGender = {gender}\nCity code = {city}\nBranch code = {branch}\nAccount type = {acc_type}\nDate of birth = {birthdate}\n")
        zloop = int(input("Please Double check the entered details: \nID and Name are final and unchangable\nif you would like to proceed, press 0\nif you would like to re-enter the details, press 1\n"))
        if zloop == 0:
            return name, password, balance, occupation, gender, city, branch, acc_type, email, birthdate, registration_time
def edit_customer(userlist):
    # Assumes staff member already knows validation rules so no further guidance will be given beyond a wrong or correct value
    skey = input("Please enter the User ID or name to search: ")
    choice = ""
    s = int()
    for i in range(len(userlist)):
        if (skey == userlist[i][0] or skey == userlist[i][1]):
            s = i
            while True:
                print(
                    f"Customer Details: \n0) ID = {userlist[i][0]}\n1) Name = {userlist[i][1]}\n2) Password = {userlist[i][2]}\n3) Starting Balance = {userlist[i][3]}\n4) Occupation = {userlist[i][4]}\n5) Gender = {userlist[i][5]}\n6) City code = {userlist[i][6]}\n7) Branch code = {userlist[i][7]}\n8) Account type = {userlist[i][8]}\n9) Email Address = {userlist[i][9]}\n10) Date of birth = {userlist[i][10]}\n")
                choice = input("ID and Name are final and unchangable so options 0/1/6/7/8 are unselectable\nWhich Detail would you like to edit:\n Press the corressponding number or 0 to exit:  ")
                if choice == "2":
                    while True:
                        password = str(input("Please enter New Password: "))
                        if len(password) >= 8:
                            break
                        else:
                            double_validation("Password must be atleast 8 digits")
                    print(f"Password: {password}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][2] = password
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "3":
                    while True:
                        balancestr = (input("Please enter New Balance: "))
                        if validate_int(balancestr) == True and int(balancestr) >= 1000:
                            balance = balancestr
                            break
                        else:
                            double_validation(
                                "Minimum input balance is 1000, Please deposit an amount greater than the minimum")
                    print(f"Balance: {balance}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][3] = balance
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "4":
                    occupation = input("New Occupation: ")
                    print(f"Occupation: {occupation}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][4] = occupation
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break


                elif choice == "5":
                    while True:
                        gender = str(input("New Gender (M or F only): ")).upper()  # M OR F
                        if gender in ['F', 'M']:
                            break
                        else:
                            double_validation("Invalid input, Please enter either M or F")
                    print(f"Gender: {gender}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][5] = gender
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "9":
                    while True:
                        email = input("Email Address: ")
                        if '@' in email and '.' in email:
                            break
                        else:
                            double_validation("Please enter you email in a proper format(user@mail.com)")
                    print(f"Email: {email}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][9] = email
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "10":
                    while True:
                        year_str = (input("Year: "))
                        if validate_int(year_str) == True and int(year_str) >= 1900 and int(year_str) <= 2005:
                            year = int(year_str)
                            break
                        else:
                            double_validation(
                                "Year is not eligible in our criteria, Please enter a year between 1900 and 2005")

                    while True:
                        month_str = (input("Month: "))
                        if validate_int(month_str) == True and int(month_str) >= 1 and int(month_str) <= 12:
                            month = int(month_str)
                            break
                        else:
                            double_validation(
                                "You may have entered the month incorrectly, Please enter a month between 1-12")

                    while True:
                        day_str = (input("Day: "))
                        if validate_int(day_str) == True and int(day_str) >= 1 and int(day_str) <= 31:
                            day = int(day_str)
                            break
                        else:
                            double_validation(
                                "You may have entered the day incorrectly, Please enter a day between 1-31")
                    rawbirthdate = datetime(year, month, day)
                    birthdate = rawbirthdate.strftime('%Y-%m-%d')
                    print(f"Date of Birth: {birthdate}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][10] = birthdate
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                else:
                    print("Editing has been canceled")
                    break
    if choice == "":
        print("User not found")
    with open("Customer_Data.txt", "w") as fh:
        for i in range(len(userlist)):
            rec = " ".join(userlist[i]) + "\n"
            fh.write(rec)
    return True
def register_staff():
    name, password, balance, occupation, gender, city, branch, acc_type, email, birthdate, registration_time = staff_registration_input()
    base_user_id = "S" + acc_type + city + branch + "0001"
    final_user_id = increment_id(base_user_id, stfdat)
    acc_history = " "
    data = ""
    password = final_user_id+"MC"
    email = final_user_id+"Majcon@mail.com"
    with open(f"{final_user_id}_history.txt", 'w') as file:
        file.write(data)
    with open(stfdat, "a") as fp:
        fp.write(f"{final_user_id} {name} {password} {balance} {occupation} {gender} {city} {branch} {acc_type} {email} {birthdate} {registration_time} {acc_history}\n")
    print(f"User registered successfully\n User ID is {final_user_id}\n Password is {password}\n Email is {email}")
    return True
#admin functions:
def admin_registration_input():
    print("Please Provide New Admin Details: ")
    zloop = 1
    while zloop == 1:
        rawname = str(input("Name: "))
        name = rawname.replace(' ', '-')
        while True:
            balancestr = (input("Starting balance: "))
            if validate_int(balancestr) == True and int(balancestr) >= 1000:
                balance = balancestr
                break
            else:
                double_validation("Minimum input balance is 1000, Please deposit an amount greater than the minimum")

        occupation = "Admin"

        while True:
            gender = str(input("Gender (M or F only): ")).upper()  # M OR F
            if gender in ['F', 'M']:
                wloop = 1
                break
            else:
                double_validation("Invalid input, Please enter either M or F")
        while True:
            citystr = (input("City.no (From 1-9 only): "))
            if validate_int(citystr) == True and 1 <= int(citystr) <= 9:
                city = '0' + str(citystr)
                break
            else:
                double_validation("Input Invalid, Please enter a number from 1-9")
        while True:
            branchstr = (input("Branch.no (From 1-9 only): "))
            if validate_int(branchstr) == True and 1 <= int(branchstr) <= 9:
                branch = '0' + str(branchstr)
                break
            else:
                double_validation("Input Invalid, Please enter a number from 1-9")
        while True:
            acc_type = str(input("Current or saving (C or S): ").upper())  # in C or S
            if acc_type in ['C', 'S']:
                break
            else:
                double_validation("Invalid account type, Please enter either C or S ONLY")
        print("Please enter your birthdate in a double digit format (e.g 29/01/2000): \n")  # general date validation
        while True:
            year_str = (input("Year: "))
            if validate_int(year_str)== True and int(year_str) >= 1900 and int(year_str) <= 2005:
                year = int(year_str)
                break
            else:
                double_validation("Year is not eligible in our criteria, Please enter a year between 1900 and 2005")

        while True:
            month_str = (input("Month: "))
            if validate_int(month_str) == True and int(month_str) >= 1 and int(month_str) <= 12:
                month = int(month_str)
                break
            else:
                double_validation("You may have entered the month incorrectly, Please enter a month between 1-12")

        while True:
            day_str = (input("Day: "))
            if validate_int(day_str) == True and int(day_str) >= 1 and int(day_str) <= 31:
                day = int(day_str)
                break
            else:
                double_validation("You may have entered the day incorrectly, Please enter a day between 1-31")
        rawbirthdate = datetime(year, month, day)
        birthdate = rawbirthdate.strftime('%Y-%m-%d')
        rawregistration_time = datetime.now()
        registration_time = rawregistration_time.strftime('%Y-%m-%d')
        password = "blank"
        email = "blank"
        print(f"Admin Details: \nName = {name}\nStarting Balance = {balance}\nOccupation = {occupation}\nGender = {gender}\nCity code = {city}\nBranch code = {branch}\nAccount type = {acc_type}\nDate of birth = {birthdate}\n")
        zloop = int(input("Please Double check the entered details: \nID and Name are final and unchangable\nif you would like to proceed, press 0\nif you would like to re-enter the details, press 1\n"))
        if zloop == 0:
            return name, password, balance, occupation, gender, city, branch, acc_type, email, birthdate, registration_time

def register_admin():
    name, password, balance, occupation, gender, city, branch, acc_type, email, birthdate, registration_time = admin_registration_input()
    base_user_id = "A" + acc_type + city + branch + "0001"
    final_user_id = increment_id(base_user_id, admdat)
    acc_history = " "
    data = ""
    password = final_user_id + "MC"
    email = final_user_id + "Majcon@mail.com"
    with open(f"{final_user_id}_history.txt", 'w') as file:
        file.write(data)
    with open(admdat, "a") as fp:
        fp.write(f"{final_user_id} {name} {password} {balance} {occupation} {gender} {city} {branch} {acc_type} {email} {birthdate} {registration_time} {acc_history}\n")
    print(f"User registered successfully\n User ID is {final_user_id}\n Password is {password}\n Email is {email}")
    return True
def edit_staff(userlist):
    # Assumes admin member already knows validation rules so no further guidance will be given beyond a wrong or correct value
    skey = input("Please enter the User ID or name to search: ")
    choice = ""
    s = int()
    for i in range(len(userlist)):
        if (skey == userlist[i][0] or skey == userlist[i][1]):
            s = i
            while True:
                print(
                    f"Staff Details: \n0) ID = {userlist[i][0]}\n1) Name = {userlist[i][1]}\n2) Password = {userlist[i][2]}\n3) Starting Balance = {userlist[i][3]}\n4) Occupation = {userlist[i][4]}\n5) Gender = {userlist[i][5]}\n6) City code = {userlist[i][6]}\n7) Branch code = {userlist[i][7]}\n8) Account type = {userlist[i][8]}\n9) Email Address = {userlist[i][9]}\n10) Date of birth = {userlist[i][10]}\n")
                choice = input("\nWhich Detail would you like to edit:\n Press the corressponding number or 0 to exit:  ")
                if choice == "1":
                    rawname = str(input("Name: "))
                    name = rawname.replace(' ', '-')
                    print(f"Name: {name}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][1] = name
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "2":
                    while True:
                        password = str(input("Please enter New Password: "))
                        if len(password) >= 8:
                            break
                        else:
                            double_validation("Password must be atleast 8 digits")
                    print(f"Password: {password}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][2] = password
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "3":
                    while True:
                        balancestr = (input("Please enter New Balance: "))
                        if validate_int(balancestr) == True and int(balancestr) >= 1000:
                            balance = balancestr
                            break
                        else:
                            double_validation(
                                "Minimum input balance is 1000, Please deposit an amount greater than the minimum")
                    print(f"Balance: {balance}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][3] = balance
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "4":
                    occupation = input("New Occupation: ")
                    print(f"Occupation: {occupation}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][4] = occupation
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break


                elif choice == "5":
                    while True:
                        gender = str(input("New Gender (M or F only): ")).upper()  # M OR F
                        if gender in ['F', 'M']:
                            break
                        else:
                            double_validation("Invalid input, Please enter either M or F")
                    print(f"Gender: {gender}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][5] = gender
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "6":
                    while True:
                        citystr = (input("New City.no (From 1-9 only): "))
                        if validate_int(citystr) == True and 1 <= int(citystr) <= 9:
                            city = '0' + str(citystr)
                            break
                        else:
                            double_validation("Input Invalid, Please enter a number from 1-9")
                    print(f"City Code: {city}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][6] = city
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "7":
                    while True:
                        branchstr = (input("New Branch.no (From 1-9 only): "))
                        if validate_int(branchstr) == True and 1 <= int(branchstr) <= 9:
                            branch = '0' + str(branchstr)
                            break
                        else:
                            double_validation("Input Invalid, Please enter a number from 1-9")
                    print(f"Branch Code: {branch}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][7] = branch
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "8":
                    while True:
                        acc_type = str(input("Current or saving (C or S): ").upper())  # in C or S
                        if acc_type in ['C', 'S']:
                            break
                        else:
                            double_validation("Invalid account type, Please enter either C or S ONLY")
                    print(f"Account Type: {acc_type}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][8] = acc_type
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "9":
                    while True:
                        email = input("Email Address: ")
                        if '@' in email and '.' in email:
                            break
                        else:
                            double_validation("Please enter you email in a proper format(user@mail.com)")
                    print(f"Email: {email}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][9] = email
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "10":
                    while True:
                        year_str = (input("Year: "))
                        if validate_int(year_str) == True and int(year_str) >= 1900 and int(year_str) <= 2005:
                            year = int(year_str)
                            break
                        else:
                            double_validation(
                                "Year is not eligible in our criteria, Please enter a year between 1900 and 2005")

                    while True:
                        month_str = (input("Month: "))
                        if validate_int(month_str) == True and int(month_str) >= 1 and int(month_str) <= 12:
                            month = int(month_str)
                            break
                        else:
                            double_validation(
                                "You may have entered the month incorrectly, Please enter a month between 1-12")

                    while True:
                        day_str = (input("Day: "))
                        if validate_int(day_str) == True and int(day_str) >= 1 and int(day_str) <= 31:
                            day = int(day_str)
                            break
                        else:
                            double_validation(
                                "You may have entered the day incorrectly, Please enter a day between 1-31")
                    rawbirthdate = datetime(year, month, day)
                    birthdate = rawbirthdate.strftime('%Y-%m-%d')
                    print(f"Date of Birth: {birthdate}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][10] = birthdate
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                else:
                    print("Editing has been canceled")
                    break
    if choice == "":
        print("User not found")
    if choice in "6,7,8":
        userlist[s][0] = "C" + userlist[s][8] + userlist[s][6] + userlist[s][7] + userlist[s][0][-4:]
    with open("Staff_Data.txt", "w") as fh:
        for i in range(len(userlist)):
            rec = " ".join(userlist[i]) + "\n"
            fh.write(rec)
    return True
def edit_admin(userlist):
    # Assumes Super user already knows validation rules so no further guidance will be given beyond a wrong or correct value
    skey = input("Please enter the User ID or name to search: ")
    choice = ""
    s = int()
    for i in range(len(userlist)):
        if (skey == userlist[i][0] or skey == userlist[i][1]):
            s = i
            while True:
                print(
                    f"Staff Details: \n0) ID = {userlist[i][0]}\n1) Name = {userlist[i][1]}\n2) Password = {userlist[i][2]}\n3) Starting Balance = {userlist[i][3]}\n4) Occupation = {userlist[i][4]}\n5) Gender = {userlist[i][5]}\n6) City code = {userlist[i][6]}\n7) Branch code = {userlist[i][7]}\n8) Account type = {userlist[i][8]}\n9) Email Address = {userlist[i][9]}\n10) Date of birth = {userlist[i][10]}\n")
                choice = input("\nWhich Detail would you like to edit:\n Press the corressponding number or 0 to exit:  ")
                if choice == "1":
                    rawname = str(input("Name: "))
                    name = rawname.replace(' ', '-')
                    print(f"Name: {name}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][1] = name
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "2":
                    while True:
                        password = str(input("Please enter New Password: "))
                        if len(password) >= 8:
                            break
                        else:
                            double_validation("Password must be atleast 8 digits")
                    print(f"Password: {password}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][2] = password
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "3":
                    while True:
                        balancestr = (input("Please enter New Balance: "))
                        if validate_int(balancestr) == True and int(balancestr) >= 1000:
                            balance = balancestr
                            break
                        else:
                            double_validation(
                                "Minimum input balance is 1000, Please deposit an amount greater than the minimum")
                    print(f"Balance: {balance}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][3] = balance
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "4":
                    occupation = input("New Occupation: ")
                    print(f"Occupation: {occupation}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][4] = occupation
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break


                elif choice == "5":
                    while True:
                        gender = str(input("New Gender (M or F only): ")).upper()  # M OR F
                        if gender in ['F', 'M']:
                            break
                        else:
                            double_validation("Invalid input, Please enter either M or F")
                    print(f"Gender: {gender}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][5] = gender
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "6":
                    while True:
                        citystr = (input("New City.no (From 1-9 only): "))
                        if validate_int(citystr) == True and 1 <= int(citystr) <= 9:
                            city = '0' + str(citystr)
                            break
                        else:
                            double_validation("Input Invalid, Please enter a number from 1-9")
                    print(f"City Code: {city}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][6] = city
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "7":
                    while True:
                        branchstr = (input("New Branch.no (From 1-9 only): "))
                        if validate_int(branchstr) == True and 1 <= int(branchstr) <= 9:
                            branch = '0' + str(branchstr)
                            break
                        else:
                            double_validation("Input Invalid, Please enter a number from 1-9")
                    print(f"Branch Code: {branch}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][7] = branch
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "8":
                    while True:
                        acc_type = str(input("Current or saving (C or S): ").upper())  # in C or S
                        if acc_type in ['C', 'S']:
                            break
                        else:
                            double_validation("Invalid account type, Please enter either C or S ONLY")
                    print(f"Account Type: {acc_type}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][8] = acc_type
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "9":
                    while True:
                        email = input("Email Address: ")
                        if '@' in email and '.' in email:
                            break
                        else:
                            double_validation("Please enter you email in a proper format(user@mail.com)")
                    print(f"Email: {email}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][9] = email
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                elif choice == "10":
                    while True:
                        year_str = (input("Year: "))
                        if validate_int(year_str) == True and int(year_str) >= 1900 and int(year_str) <= 2005:
                            year = int(year_str)
                            break
                        else:
                            double_validation(
                                "Year is not eligible in our criteria, Please enter a year between 1900 and 2005")

                    while True:
                        month_str = (input("Month: "))
                        if validate_int(month_str) == True and int(month_str) >= 1 and int(month_str) <= 12:
                            month = int(month_str)
                            break
                        else:
                            double_validation(
                                "You may have entered the month incorrectly, Please enter a month between 1-12")

                    while True:
                        day_str = (input("Day: "))
                        if validate_int(day_str) == True and int(day_str) >= 1 and int(day_str) <= 31:
                            day = int(day_str)
                            break
                        else:
                            double_validation(
                                "You may have entered the day incorrectly, Please enter a day between 1-31")
                    rawbirthdate = datetime(year, month, day)
                    birthdate = rawbirthdate.strftime('%Y-%m-%d')
                    print(f"Date of Birth: {birthdate}")
                    while True:
                        reply = input("Are you sure you would like to proceed?\n press 1 to proceed or 0 to exit: ")
                        if reply == "1":
                            userlist[i][10] = birthdate
                            print("Update successful")
                            break
                        elif reply == "0":
                            print("Update unsuccessful")
                            break
                        else:
                            double_validation("Invalid input, press 1 to proceed or 0 to exit: ")
                    break
                else:
                    print("Editing has been canceled")
                    break
    if choice == "":
        print("User not found")
    if choice in "6,7,8":
        userlist[s][0] = "C" + userlist[s][8] + userlist[s][6] + userlist[s][7] + userlist[s][0][-4:]
    with open("Admin_Data.txt", "w") as fh:
        for i in range(len(userlist)):
            rec = " ".join(userlist[i]) + "\n"
            fh.write(rec)
    return True
#main menu functions:

def withdraw(balanceh,userlist,file,line,acc_type,ID):
    confirm = True
    balance = balanceh
    print(" Withdrawal menu\n","How much money would you like to withdraw?")
    print(" 1) 50\n" ,"2) 100\n","3) 150\n","4) 200\n","5) 250\n", "6) 300\n", "7) 350\n","8) 400\n" ,"9) 450\n", "10) 500\n","11) Custom ")
    select = int(input("Please select an option: "))
    if select == 1:
        balance = balance - 50
    elif select == 2:
        balance = balance - 100
    elif select == 3:
        balance = balance - 150
    elif select == 4:
        balance = balance - 200
    elif select == 5:
        balance = balance - 250
    elif select == 6:
        balance = balance - 300
    elif select == 7:
        balance = balance - 350
    elif select == 8:
        balance = balance - 400
    elif select == 9:
        balance = balance - 450
    elif select == 10:
        balance = balance - 500
    elif select == 11:
        customwithdraw = int(input("How much would you like to withdraw? "))
        balance = balance - customwithdraw
    else:
        print("You have selected an invalid option, you will be returned to the main menu")
        confirm = False
    if acc_type == "Current":
        if balance < 500:
            print("Balance is insufficient, transaction has been canceled")
            confirm = False
    if acc_type == "Saving":
        if balance < 100:
            print("Balance is insufficient, transaction has been canceled")
            confirm = False
    if confirm == True:
        print("Your current balance is: ", balance)
        delta = balanceh - balance
        userlist[line][3] = str(balance)
        with open(file, "w") as fh:
            for i in range(len(userlist)):
                rec = " ".join(userlist[i]) + "\n"
                fh.write(rec)
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%Y-%m-%d')
        formatted_time = current_datetime.strftime('%H:%M')
        trans_history = add_new_transaction(load_transaction_history(f"{ID}_history.txt"), formatted_date,
                                            formatted_time,
                                            'Transaction_type:Withdrawal', delta)
        save_transaction_history(trans_history, f"{ID}_history.txt")
        balanceh = balance
        print("Withdrawal successful")
    else:
        print("Withdrawal unsuccessful")
    return False, balanceh
def deposit(balance,userlist,file,line,ID):
    while True:
        custom_deposit = (input("How much would you like to deposit? "))
        if validate_int(custom_deposit) == True and len(str(custom_deposit)) <= 4:
            balance += int(custom_deposit)
            print("Your current balance is ", balance)
            userlist[line][3]= str(balance)
            with open(file, "w") as fh:
                for i in range(len(userlist)):
                    rec = " ".join(userlist[i]) + "\n"
                    fh.write(rec)
            print("Deposit successful")
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            formatted_time = current_datetime.strftime('%H:%M')
            trans_history = add_new_transaction(load_transaction_history(f"{ID}_history.txt"), formatted_date, formatted_time,
                                'Transaction_type:Deposit', custom_deposit)
            save_transaction_history(trans_history, f"{ID}_history.txt")
            return False, balance
        elif len(str(custom_deposit)) > 4 or validate_int(custom_deposit) == False:
            double_validation("The number you entered is above the limit. Please Deposit a smaller value or please visit your nearest branch if you want to deposit a value greater than 9,999.")


def Acc_statement(ID):
    for i in range(0,2):
        if i == 0:
            print("Please enter Start Date: ")
        elif i == 1:
            print("Please enter End Date: ")
        while True:
            year_str = (input("Year: "))
            if validate_int(year_str) == True and int(year_str) >= 1900 and int(year_str) <= 3000:
                year = int(year_str)
                break
            else:
                double_validation(
                    "Year is not eligible in our criteria, Please enter a year between 1900 and 3000")

        while True:
            month_str = (input("Month: "))
            if validate_int(month_str) == True and int(month_str) >= 1 and int(month_str) <= 12:
                month = int(month_str)
                break
            else:
                double_validation(
                    "You may have entered the month incorrectly, Please enter a month between 1-12")

        while True:
            day_str = (input("Day: "))
            if validate_int(day_str) == True and int(day_str) >= 1 and int(day_str) <= 31:
                day = int(day_str)
                break
            else:
                double_validation(
                    "You may have entered the day incorrectly, Please enter a day between 1-31")
        rawdate = datetime(year, month, day)
        if i == 0:
            start_date = rawdate.strftime('%Y-%m-%d')
        elif i == 1:
            end_date = rawdate.strftime('%Y-%m-%d')
    print(load_transaction_history(f"{ID}_history.txt"))
    return False
def Global_Acc_statement(userlist):
    skey = input("Please enter the User ID or name to search: ")
    choice = ""
    s = int()
    for i in range(len(userlist)):
        if (skey == userlist[i][0] or skey == userlist[i][1]):
            Acc_statement(skey)
    return False

def Customer_Menu(balance,userdata,file,line,acc_type,ID):
    outererror = True #exit variable, program exits if value is -1
    while outererror == True:
        print("Customer menu:")
        print(" 1) Deposit\n", "2) Withdraw\n", "3) Generate account statement\n", "5) Exit")
        choice = (input("Please enter your choice: "))
        if choice == "1":
            # Define the Deposit() function or remove the call if not implemented
            outererror, balance = deposit(balance,userdata,file,line,ID)
        elif choice == "2":
            # Define the Withdraw() function or remove the call if not implemented
            outererror, balance = withdraw(balance,userdata,file,line,acc_type,ID)
        elif choice == "3":
           outererror = Acc_statement(ID)
        elif choice == "5":
            outererror = False
        else:
            while True:
                print("You have entered an invalid number. Would you like to exit or try again?\n",
                      "0) Exit\n", "1) Try again")
                choice1 = (input("Please enter your choice: "))
                if choice1 == "0":
                    outererror = False
                    break
                elif choice1 == "1":
                    outererror = True
                    break
    print("Goodbye, and Thank you for using Majima Construction Bank Services!")
    return True
def Staff_Menu(balance,userdata,file,line,acc_type,ID):
    outererror = True #exit variable, program exits if value is False
    while outererror == True:
        print("Staff menu:")
        print(" 1) Create Customer\n", "2) Edit Customer\n", "3) Generate Customer report\n", "4) Personal Menu\n", "5) Exit")
        choice = (input("Please enter your choice: "))
        if choice == "1":
            outererror = register_customer()
        elif choice == "2":
            outererror = edit_customer(customer_database())
        elif choice == "3":
            outererror = Global_Acc_statement(customer_database())
        elif choice == "4":
            outererror = Customer_Menu(balance,userdata,file,line,acc_type,ID)
        elif choice == "5":
            outererror = False
        else:
            while True:
                print("You have entered an invalid number. Would you like to exit or try again?\n",
                      "0) Exit\n", "1) Try again")
                choice1 = (input("Please enter your choice: "))
                if choice1 == "0":
                    outererror = False
                    break
                elif choice1 == "1":
                    outererror = True
                    break
    print("Goodbye, and Thank you for using Majima Construction Bank Services!")
    return True
def Admin_Menu(balance,userdata,file,line,acc_type,ID):
    outererror = True #exit variable, program exits if value is False
    while outererror == True:
        print("Admin menu:")
        print("1) Register Staff\n","2) Edit Staff\n","3) Create Customer\n", "4) Edit Customer\n", "5) Generate Customer report\n", "6) Generate Staff report\n", "7) Personal Menu\n", "8) Exit")
        choice = (input("Please enter your choice: "))
        if choice == "1":
            outererror = register_staff()
        elif choice == "2":
            outererror = edit_staff(staff_database())
        elif choice == "3":
            outererror = register_customer()
        elif choice == "4":
            outererror = edit_customer(customer_database())
        elif choice == "5":
            outererror = Global_Acc_statement(customer_database())
        elif choice == "6":
            outererror = Global_Acc_statement(staff_database())
        elif choice == "7":
            outererror = Customer_Menu(balance,userdata,file,line,acc_type,ID)
        elif choice == "8":
            outererror = False
        else:
            while True:
                print("You have entered an invalid number. Would you like to exit or try again?\n",
                      "0) Exit\n", "1) Try again")
                choice1 = (input("Please enter your choice: "))
                if choice1 == "0":
                    outererror = False
                    break
                elif choice1 == "1":
                    outererror = True
                    break
    print("Goodbye, and Thank you for using Majima Construction Bank Services!")
    return True
def Super_Menu(balance,userdata,file,line,acc_type,ID):
    outererror = True #exit variable, program exits if value is False
    while outererror == True:
        print("Super_User menu:")
        print("1) Register Admin\n","2) Edit Admin\n","3) Register Staff\n","4) Edit Staff\n","5) Create Customer\n", "6) Edit Customer\n", "7) Generate Customer report\n", "8) Personal Menu\n", "9) Exit")
        choice = (input("Please enter your choice: "))
        if choice == "1":
            outererror = register_admin()
        elif choice == "2":
            outererror = edit_admin(admin_database())
        elif choice == "3":
            outererror = register_staff()
        elif choice == "4":
            outererror = edit_staff(staff_database())
        elif choice == "5":
            outererror = register_customer()
        elif choice == "6":
            outererror = edit_customer(customer_database())
        elif choice == "7":
            outererror = Global_Acc_statement(customer_database())
        elif choice == "8":
            outererror = Customer_Menu(balance,userdata,file,line,acc_type,ID)
        elif choice == "9":
            outererror = False
        else:
            while True:
                print("You have entered an invalid number. Would you like to exit or try again?\n",
                      "0) Exit\n", "1) Try again")
                choice1 = (input("Please enter your choice: "))
                if choice1 == "0":
                    outererror = False
                    break
                elif choice1 == "1":
                    outererror = True
                    break
    print("Goodbye, and Thank you for using Majima Construction Bank Services!")
    return True
def master_login():
    while True:
        ID, password = ask_user_credentials()
        user_type = ""
        Acc_type = ""
        allusers = []
        if ID[0] == "C":
            user_type = "Customer"
            allusers = customer_database()
        elif ID[0] == "S":
            user_type = "Staff"
            allusers = staff_database()
        elif ID[0] == "A":
            user_type = "Admin"
            allusers = admin_database()
        elif ID[0] == "U":
            user_type = "Super User"
            allusers = SuperUser_database()
        if ID[1] == "S":
            Acc_type = "Saving"
        elif ID[1] == "C":
            Acc_type = "Current"
        if validate_int(ID[-4:]) == True:
            line_no = int(ID[-4:]) - 1
            if allusers[line_no][2] == password and allusers[line_no][0] == ID:
                balance = int(allusers[line_no][3])
                name = allusers[line_no][1]
                valid = True
                return user_type, Acc_type, line_no, balance, valid, allusers, ID, name
            else:
                    valid = False
                    double_validation("You have entered an invalid username or password")
        else:
            double_validation("You have entered an invalid username or password")
#Start of main code
print("Welcome to Majima Construction Bank")
user_type, Acc_type, line_no, balance, valid, userdata, USR_ID, name = master_login()
if valid == True:
    print(f"Welcome back {name}")
    if user_type == "Customer":
        Customer_Menu(balance,userdata,cusdat,line_no, Acc_type,USR_ID)
    elif user_type == "Staff":
        Staff_Menu(balance,userdata,stfdat,line_no, Acc_type,USR_ID)
    elif user_type == "Admin":
        Admin_Menu(balance,userdata,stfdat,line_no, Acc_type,USR_ID)
    elif user_type == "Super User":
        Super_Menu(balance,userdata,stfdat,line_no, Acc_type,USR_ID)

