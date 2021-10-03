import dbactions as db

while True:
    print("**************MENU**************")
    print("1. Registration")
    print("2. Login")
    print("3. Forgot Password")
    print("4.EXIT")
    user_choice = int(input("Enter your choice\n"))
    if user_choice == 1:
        uname = input("Enter your Email\n")
        pwd = input("Enter your Password\n")
        db.registration(uname, pwd)
    elif user_choice == 2:
        uname = input("Enter your Email\n")
        pwd = input("Enter your Password\n")
        db.login(uname, pwd)
    elif user_choice == 3:
        uname = input("Enter your Email\n")
        db.forgot_pwd(uname)
    else:
        break
