import random
import string

try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        # Combine all character types
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        print("Generated password:", password)

except ValueError:
    print("Invalid input. Please enter a valid integer.")
