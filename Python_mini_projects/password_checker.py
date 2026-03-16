"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""
import string
import random
import getpass

password = getpass.getpass("Please Enter Your 8 Character Password . It should include\n1. Length (at least 8 characters)\n2. At least one uppercase letter\n3. At least one lowercase letter\n4. At least one digit\n5. At least one special character (e.g., @, #, $, etc.)\n")
        
def password_check():
    password_dict = {}
    upperChar = any(ch.isupper() for ch in password)
    lowerChar = any(ch.islower() for ch in password)
    digit = any(ch.isdigit() for ch in password)
    special_char = any(ch in string.punctuation for ch in password)
    
    password_dict["UpperCaseCharacter"] = upperChar
    password_dict["LowerCaseCharacter"] = lowerChar
    password_dict["Numbers"] = digit
    password_dict["SpecialChar"] = special_char

    failed_check = [key for key, value in password_dict.items() if value == False]
    if failed_check:
        print("Password Check got failed")
        print("You have these missing parameters in your password:", ",".join(failed_check))
        print("Choose Different Password!!!")
        
        chance = input("DO you want to try again (y/n):").lower().strip()
        if chance == "y":
            password_check()        
    else:
        print("All Condition Passed!!!")
        
def ready_password():
    length = 8
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    special_char = string.punctuation
    
    required = upper + lower + numbers + special_char
    password = [random.choice(upper),random.choice(lower),random.choice(numbers),random.choice(special_char)]
    password += random.choices(required, k=length - 4)
    random.shuffle(password)
    return "".join(password)

while True:
    if len(password) >= 8:
        print("Password is 8 Char or above. Checking the validity of the password.")
        if password_check():
            pass
        else:
            break
    else:
        print("Your password is not 8 char long. Choose from below")
        auto_create_password = input("Do you want your password to be autocreated (y/n):\n").lower().strip()
        if auto_create_password == "y":
            output = ready_password()
            print(f"Your new 8 Char password is: {output}")
            break
        else:
            print("Thank You!!! Byee....")
            break