import re
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    return score, suggestions


# ===== Main Program =====
password = input("Enter your password: ")

score, suggestions = check_password_strength(password)

if score <= 2:
    print("Strength: WEAK")
elif score <= 4:
    print("Strength: MEDIUM")
else:
    print("Strength: STRONG")

if suggestions:
    print("Suggestions:")
    for s in suggestions:
        print("-", s)

hashed = hash_password(password)
print("Hashed Password:", hashed)
