import re


def email_validate(email):
    regex = '^[a-z0-9A-Z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        print("Enter a valid Mail")
        return False


def pwd_validate(pwd):
    temp = True
    special_char = 0
    low_case = up_case = digits = 0
    if not 5 < len(pwd) < 16:
        print("Minimum Length of password is 5 and maximum is 16 ")
        temp = False
    for i in pwd:
        if i.isdigit():
            digits = digits + 1
        elif i.islower():
            low_case = low_case + 1
        elif i.isupper():
            up_case = up_case + 1
        else:
            special_char = special_char + 1
    if digits == 0 or low_case == 0 or up_case == 0 or special_char == 0:
        temp = False
        print('Password should contain at least one special character, one lower case character, one upper case '
              'character '
              'one digit')
        print("Enter a valid password")
    return temp
