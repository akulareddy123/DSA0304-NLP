import re

# Validation patterns

register_pattern = r"^\d{2}[A-Z]{3}\d{3}$"

email_pattern = r"^\d{2}[a-zA-Z]{3}\d{3}@university\.edu$"

course_pattern = r"^[A-Z]{3}\d{3}$"

semester_pattern = r"^Semester [1-8]$"

mobile_pattern = r"^[6-9]\d{9}$"


# Validation function
def validate_field(pattern, value):
    return bool(re.fullmatch(pattern, value))


# Get student details
print("===== UNIVERSITY REGISTRATION SYSTEM =====")

register_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")


# Validate Register Number
if validate_field(register_pattern, register_no):
    print("Register Number: Valid")
else:
    print("Register Number: Invalid")


# Validate Email
if validate_field(email_pattern, email):
    print("Institutional Email: Valid")
else:
    print("Institutional Email: Invalid")


# Validate Course Code
if validate_field(course_pattern, course):
    print("Course Code: Valid")
else:
    print("Course Code: Invalid")


# Validate Semester
if validate_field(semester_pattern, semester):
    print("Semester: Valid")
else:
    print("Semester: Invalid")


# Validate Mobile Number
if validate_field(mobile_pattern, mobile):
    print("Mobile Number: Valid")
else:
    print("Mobile Number: Invalid")


# Final status
all_valid = (
    validate_field(register_pattern, register_no)
    and validate_field(email_pattern, email)
    and validate_field(course_pattern, course)
    and validate_field(semester_pattern, semester)
    and validate_field(mobile_pattern, mobile)
)

print("\n===== REGISTRATION STATUS =====")

if all_valid:
    print("Registration Successful!")
    print("All student details are valid.")
else:
    print("Registration Failed!")
    print("Please correct the invalid fields.")