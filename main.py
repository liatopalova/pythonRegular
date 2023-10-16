import re

print("1. Phone_number\n2. Mobile_number\n3. Email\n4. Full_name\n")
user_select = int(input("Enter menu item: "))


def validate_phone_number(number):
    current_num = re.sub(r'\D', '', number)
    pattern = r'^[0-9]{5,10}$'
    if re.match(pattern, current_num):
        return True
    else:
        return False


def validate_mobile_number(number):
    pattern = r'^[+]{0,1}\d{,2}?[\s]?\(?\d{3}\)?[-\s]?\d{3}?[-\s]?\d{2}?[-\s]?\d{2}$'
    if re.match(pattern, number):
        return True
    else:
        return False


def validate_email(email):
    pattern = r'^(?=.{10,30}$)[\w.-]+@[A-Za-z]+\.(com|net|org)$'
    if re.match(pattern, email):
        return True
    else:
        return False


def validate_full_name(name):
    pattern = r'^[A-Za-zА-Яа-я]{2,20}?[\s]?([\s][A-Za-zА-Яа-я]{2,20}){0,2}?[\s]?$'
    if re.match(pattern, name):
        return True
    else:
        return False


match user_select:
    case 1:
        phone_number = input("Enter phone number: ")
        print(validate_phone_number(phone_number))
    case 2:
        mobile_number = input("Enter mobile number: ")
        print(validate_mobile_number(mobile_number))
    case 3:
        user_email = input("Enter email: ")
        print(validate_email(user_email))
    case 4:
        full_name = input("Enter name: ")
        print(validate_full_name(full_name))
    case _:
        print("Select menu item!")
