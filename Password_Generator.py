# Password Generator
import random 
import string 

def generate_password(length = 6):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    character = lower + upper + digits + special

    password += [random.choice(character)for _ in range(length - 4)]

    random.shuffle(password)

    return ''.join(password)

user_input = int(input("Enter required password length: "))
print("Password Generated is :", generate_password(user_input))
   
