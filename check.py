import re
"""
The example regular expression matches "^\w+@\w+.\w+$" pattern, where:
"^" - start of the string
"\w" - matches any alphanumeric character
"+" - is quantifier (match one or more occurences)
"@" - matches the character "@" literally
"$" - end of the string

for more information --> https://www.dataquest.io/blog/regex-cheatsheet
"""
def checkemail(address):
    is_valid=re.search('^\w+@\w+.(com)+$', address)
    if is_valid:
        return True
    else:
        print('It looks that provided mail is not in correct format. \n'
              'Please make sure that you have "@" and "." in your address \n'
              'and the length of your mail is at least 6 characters long')
        return False

mail = input("Email:")
while not checkemail(mail):
    mail = input("Email:")
else:
    print("if email is correct do whatever you want in this field")
