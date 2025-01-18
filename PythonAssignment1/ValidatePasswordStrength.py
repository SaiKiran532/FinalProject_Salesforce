import re


def validate_password_strength(password):

    if len(password) <= 8 or len(password) >= 15:
        return "Password must be greater than 8 and less than 15 characters."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return "Password is strong."

Password = input("Enter Password:")
print(validate_password_strength(Password))
