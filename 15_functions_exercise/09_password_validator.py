import re

password_input = input()


def password_validator(password):
    if len(password) not in range(6, 10 + 1):
        return "Password must be between 6 and 10 characters"
    #  if it contains only letters and nums ot will return True
    check = bool(re.match("^[A-Za-z0-9]*$", password))
    if not check:
        return "Password must consist only of letters and digits"
    #  counts how many digits we have in the password
    occurrence = 0
    for char in password:
        if char.isdigit():
            occurrence += 1
    if occurrence < 2:
        return "Password must have at least 2 digits"

    #  if we pass all checks
    return "Password is valid"


print(password_validator(password_input))
