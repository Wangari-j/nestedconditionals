password = input("password: ")

if len(password) > 8:
    if any(number in password for number in "9876543210"):
        if password != password.lower():
            if password != password.upper():
                print("password valid. Account created.")
            else:
                print("password must contain a lowercase")
        else:
            print("password must contain an uppercase letter")
    else:
        print("password must contain a number")
else:
    print("password too short, must be more than 8 characters")
