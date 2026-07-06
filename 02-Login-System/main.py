correct_username = "admin"
correct_password = "1234"

attempts = 1

while attempts <= 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Success!")
        break
    else:
        print("Invalid username or Password. Please try again!")
        attempts = attempts + 1
if attempts > 3:
    print("Too many invalid arttempts, Please try again later.")