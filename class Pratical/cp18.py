import re
def check_expression(expression):
    pattern = r'^(AND|OR|NOT|FORALL|EXISTS)?\s*\(?[A-Za-z]+\([a-zA-Z,\s]+\)\)?$'
    return bool(re.fullmatch(pattern, expression.strip(), re.IGNORECASE))

expression = input("Enter logical expression: ")

if check_expression(expression):
    print("Valid basic logical expression")
else:
    print("Invalid logical expression")