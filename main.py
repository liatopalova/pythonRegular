import re


def validate_phone_number(number):
    current_num = re.sub(r'\D', '', number)
    pattern = r'^[0-9]{5,10}$'
    if re.match(pattern, current_num):
        return True
    else:
        return False


print(validate_phone_number("0462 5-18-28"))


def validate_mobile_number(number):
    pattern = r'^[+]{0,1}?\d{2}?[\s]?\(?\d{3}\)?[-\s]?\d{3}?[-\s]?\d{2}?[-\s]?\d{2}$'
    if re.match(pattern, number):
        return True
    else:
        return False


print(validate_mobile_number("+38(093)519 67 78"))


def validate_email(email):
    pattern = r'^(?=.{10,30}$)[\w.-]+@[A-Za-z]+\.(com|net|org)$'
    if re.match(pattern, email):
        return True
    else:
        return False


print(validate_email("lia.topalova@gmail.com"))


def validate_full_name(name):
    pattern = r'^[A-Za-zА-Яа-я]{2,20}?[\s]?([\s][A-Za-zА-Яа-я]{2,20}){0,2}?[\s]?$'
    if re.match(pattern, name):
        return True
    else:
        return False


print(validate_full_name("Топалова Lia "))



