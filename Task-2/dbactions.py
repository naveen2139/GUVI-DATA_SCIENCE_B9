import mysql.connector as connection
import validation as v

con = connection.connect(host="localhost", username="root", password="", database="practise")
cursor = con.cursor()


def registration(uname, pwd):
    insert_stmt = "insert into registration(username,pwd)Values(%s,%s)"
    e_valid = v.email_validate(uname)
    p_valid = v.pwd_validate(pwd)
    if e_valid and p_valid:
        cursor.execute(insert_stmt, (uname, pwd))
        con.commit()
        print("Email and Password updated in the database Successfully")


def login(uname, pwd):
    search_stmt = "select * from registration where username=%(uname)s"
    cursor.execute(search_stmt, {'uname': uname})
    password = cursor.fetchone()
    if password is None:
        print("Please Register before you login")
    elif pwd == password[1]:
        print("Login Successful")
    else:
        print("Wrong Password")


def forgot_pwd(uname):
    search_stmt = "select * from registration where username=%(uname)s"
    cursor.execute(search_stmt, {'uname': uname})
    pwd = cursor.fetchone()
    if pwd is None:
        print("Please Register ")
    else:
        print("Your Password:" + pwd[1])
