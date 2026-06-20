from services.user_service import create_user

def main():
    print("-------WELCOME TO THE PC PARTS EXPLORER-------\n")
    print("What would you like to do?\n")
    print(" 1. Login\n 2. Register\n 3. Update Information\n 4. Delete Account")

    choice = int(input("Please enter your input: "))

    if choice == 1:
        # login()
        pass

    elif choice == 2:
        register_user()
    
    elif choice == 3:
        # update_credentials()
        pass

    elif choice == 4:
        # delete_account()
        pass

    else:
        raise ValueError("Invalid input, try again.")


def register_user():
    print("-------REGISTER-------\n")
    username = input("Enter your username:")
    email = input("Enter your email:")
    full_name = input("Enter your full name:")
    password = input("Enter your password:")
    create_user(username, email, full_name, password)


main()