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
