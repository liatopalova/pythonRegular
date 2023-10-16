import re


def validate_phone_number(number):
    current_num = re.sub(r'\D', '', number)
    pattern = r'^[0-9]{5,10}$'
    if re.match(pattern, current_num):
        return True
    else:
        return False


print(validate_phone_number("0462 5-18-28"))
