import re

password = input("Enter your password: ")
score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[0-9]", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1


# Strength result
if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")