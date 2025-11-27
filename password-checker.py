import re

def check_password(pwd):
    strength = 0
    remarks = ""

    # Length
    if len(pwd) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Contains digits
    if re.search(r"\d", pwd):
        strength += 1
    else:
        remarks += "Password should include at least one number.\n"

    # Uppercase
    if re.search(r"[A-Z]", pwd):
        strength += 1
    else:
        remarks += "Password should include an uppercase letter.\n"

    # Special characters
    if re.search(r"[!@#$%^&*]", pwd):
        strength += 1
    else:
        remarks += "Password should include a special character (!@#$%^&*).\n"

    if strength == 4:
        return "Strong Password "
    elif strength == 3:
        return "Moderate Password "
    else:
        return "Weak Password \n" + remarks

pwd = input("Enter password to check: ")
print(check_password(pwd))
