names = []

while True:
    print("1. Create list / 2. Read list / 3. Update list / 4. Delete list ")
    user = int(input("Choose option: "))

    if user == 1:
        name = input("Enter your name: ")
        names.append(name)
        number = input("Enter your mobile number: ")
        while len(number) != 10 or not number.isdigit():
            print("Invalid mobile number. Please enter a 10-digit number.")
            number = input("Enter your mobile number: ")
        names.append(number)

        gmail = input("Enter your gmail: ")
        while gmail.count('@') != 1 or '.' not in gmail.split('@')[1]:
            print("Invalid email address. Please enter a valid email.")
            gmail = input("Enter your gmail: ")
        names.append(gmail)

        password = input("Enter your password: ")
        while len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            print("Invalid password. Please enter a strong password.")
            password = input("Enter your password: ")

        names.append(password)
        print("Your data has been filled!")

    elif user == 2:
        if not names:
            print("No data available.")
            continue

        check = input("Enter your password: ")
        if check == names[3]:  
            print("Your data is:")
            print("Full Name:", names[0])
            print("Mobile Number:", names[1])
            print("Email Address:", names[2])
            print("Password:", names[3])

            
        else:
            print("Incorrect password. Please set a password.")

    elif user == 3:
        print("Choose data to update:")
        print("1. Name\n2. Number\n3. Gmail\n4. Password")
        nikil = int(input("Enter your choice: "))

        if 1 <= nikil <= 4:
            new_data = input(f"Enter your new {names[nikil - 1]}: ")
            names[nikil - 1] = new_data
        else:
            print("Invalid choice. Please enter a valid number.")

    elif user == 4:
        confirm = input("Are you sure you want to delete all data? (y/n): ")
        if confirm.lower() == "y":
            z = input("Enter your password: ")
            if z == names[3]:  
                names.clear()
                print("Your data has been deleted.")
            else:
                print("Incorrect password. Deletion failed.")
        else:
            print("Data deletion canceled.")

    else:
        print("Invalid option. Please choose a valid option.")
