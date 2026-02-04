import re
import hashlib
import json
import getpass



# Load users from file (if exists), else start empty
try:
    with open("users.json", "r") as f:
        users_db = json.load(f)
except FileNotFoundError:
    users_db = {}

# Save users dictionary to file
def save_users():
    with open("users.json", "w") as f:
        json.dump(users_db, f)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    return score, suggestions
def register():
    username = input("Enter a username: ")

    if username in users_db:
        print("Username already exists!")
        return

    password = getpass.getpass("Enter password: ")
    score, suggestions = check_password_strength(password)

    if score <= 4:
        print("Password is too weak. Suggestions:")
        for s in suggestions:
            print("-", s)
        return

    hashed = hash_password(password)
    users_db[username] = hashed
    print("Registration successful!")

    users_db[username] = hashed
    save_users()

def login():
    username = input("Enter username: ")

    if username not in users_db:
        print("Username does not exist!")
        return

    password = getpass.getpass("Enter a password: ")
    hashed = hash_password(password)

    if users_db[username] == hashed:
        print("Login successful!")
    else:
        print("Incorrect password!")
while True:
    print("\n--- MENU ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
