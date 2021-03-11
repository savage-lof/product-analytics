import re


def check_password(password):
    if len(password) >= 7:
        if password.isalnum() and re.search(r'\D', password):
            if password.islower() == False and password.isupper() == False:
                if re.search(r'[a-zA-Z0-9]', password):
                    if len(set(password)) == len(password):
                        return True
    return False
