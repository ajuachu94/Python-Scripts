
import secrets
import string

alpha_set = string.ascii_letters
num_set = string.digits
char_set = ['!', '@', '$', '%', '^', '&', '*', '(', ')', '/', '~']
#print(secrets.choice(char_set))

option = int(input("Welcome to password generator cum strength checker \n Kindly choose your required option from below: \n 1. Password generator \n 2. Password strength checker\n "))

if (option == 1):

    length = int(input("Enter password length (ideally more than 8):"))
    
    password = ""
    
    l = 0
    while (l<length):
        password += secrets.choice(alpha_set)
        password += secrets.choice(num_set)
        password += secrets.choice(char_set)
        l += 1
    
    print ("The generated password is: ", password)
elif (option ==2):
    new_pass = input("Enter you password:\n")
    flag = 10
    upper = 0
    lower = 0
    digit = 0
    char = 0
    if (len(new_pass)<=8):
        flag -= 1
    for c in new_pass:
        if (c.isupper()):
            upper = 1
            break
    for c in new_pass:
        if (c.islower()):
            lower = 1
            break
    for c in new_pass:
        if (c.isdigit()):
            digit = 1
    if (upper == 0 or lower == 0):
        flag -= 1
    if (digit == 0):
        flag -= 1
    for c in new_pass:
        if (c in char_set):
            char = 1
            break
    if (char == 0):
        flag -= 1
    print ("Your password strength on a scale of 1 to 10:\n", flag)
    
    