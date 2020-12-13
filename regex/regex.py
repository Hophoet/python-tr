import re


def is_valid_email(email):
    pattern = r'[a-zA-Z]+@[a-zA-Z]+(.[a-zA-Z]+)$'
    match = re.match(pattern, email)
    if(match):
        return True
    return False


def is_valid_number(number):
    pattern = r'228 ([0-9]{2}[- ]){3}[0-9]{2}$'
    match = re.match(pattern, number)
    if(match):
        return True
    return False


def is_valid_password(password):
    pattern = r'([a-z]+[A-Z]+[0-9]+)|([A-Z]+[a-z]+[0-9]+)'
    match = re.match(pattern, password)
    if(match):
        return True
    return False