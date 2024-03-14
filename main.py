import random
import string
is_on = True
print("Welcome to the Password Generator!")

password_length = int(input("How many characters should your password have? "))

print("""
Here's the list of the character types that your password can include:
1. Letters
2. Numbers
3. Special characters""")

character_set = ""

while is_on:
    choice = int(input("Choose a number. You will be able to pick multiple, but pick one at a time. Press 4 to finish: "))
    if choice == 1:
        character_set += string.ascii_letters
    elif choice == 2:
        character_set += string.digits
    elif choice == 3:
        character_set += string.punctuation
    elif choice == 4:
        is_on = False
    else:
        print("Sorry, t10he choice was incorrect. Please try again.")

password = []

for i in range(password_length):
    char = random.choice(character_set)
    password.append(char)

print(f"Your password is: " + "".join(password))