import re

# Email validation
email_pattern = r"^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$"

# Password validation
password_pattern = (
    r"^(?=.*[A-Z])"
    r"(?=.*[a-z])"
    r"(?=.*\d)"
    r"(?=.*[@#$%&!])"
    r".{8,}$"
)

# Mobile validation
mobile_pattern = r"^[6-9]\d{9}$"


# Get input
email = input("Enter Email Address: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")


# Validate Email
if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# Validate Password
if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")


# Validate Mobile
if re.fullmatch(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")