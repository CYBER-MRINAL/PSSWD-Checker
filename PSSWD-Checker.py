#!/usr/bin/env python3
import re
import math
import hashlib
import requests
import subprocess
from collections import Counter
import random
import string

# Hello This is CYBER-MRINAL. Welcome to My Code View.

# Run figlet with the specified options
subprocess.run(["figlet", "PSSWD-Checker"])
print('>>---S-T-A-R-T-E-D---<<\n')

# A more extensive list of common passwords (this can be expanded)
COMMON_PASSWORDS = set([
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "1234567890", "qwerty", "abc123", "password1", "123123", "admin",
    "letmein", "welcome", "login", "1q2w3e4r", "princess", "sunshine",
    "iloveyou", "trustno1", "123456a", "monkey", "shadow", "master",
    "michael", "superman", "jordan", "harley", "football", "1234", "12345678",
    "qwertyuiop", "123321", "1qaz2wsx", "password123", "qwerty123", "abc123456",
    "123", "123123123", "qwertyui", "1q2w3e", "letmein123", "welcome1",
    "admin123", "password1234", "password1", "qwerty1", "1234abcd", "1qaz@wsx",
    "qwerty1234", "abc12345", "monkey123", "iloveyou123", "12345abc", "123abc",
    "qwerty!@#", "password!", "letmein!", "123456789a", "qwerty!@#$", "1qaz2wsx3edc",
    "qwerty12345", "password12", "12345678910", "qwerty123456", "123456qwerty",
    "qwertyabc", "passwordabc", "1234567a", "qwerty1!", "abc!@#123", "1qazxsw2",
    "qwertyuiop123", "password!@#", "1234qwer", "qwerty12345!", "letmein1234",
    "1234567890qwerty", "qwerty123456789", "password12345", "123456789abc",
    "qwerty12345678", "123456789qwerty", "qwertyabc123", "password1!", "12345!",
    "qwerty123!", "letmein123!", "12345678!", "password123!", "123456789!",
    "qwerty1234!", "abc123!", "1234password", "passwordabc123", "1234567890!",
    "qwertyuiop!", "1234567!", "qwerty1@", "letmein1", "1234qwerty", "qwerty12345@",
    "password123456", "1234567890abc", "qwertyabc!", "1234567890qwertyuiop",
    "qwerty1234567", "password123456789", "1234567890password", "qwerty1234567890",
    "letmein12345", "1234567890qwerty123", "qwerty123456789a", "passwordqwerty",
    "1234567890abcde", "qwertyuiop12345", "password1234!", "1234567890qwertyui",
    "qwerty123456789!", "1234567890qwerty12345", "password123456789",
    "qwerty1234567890", "1234567890qwertyui", "qwerty12345678901", "letmein123456",
    "1234567890qwertyuiop", "qwerty123456789012", "password1234567", "1234567890abc123",
    "qwertyuiop123456", "password12345678", "1234567890qwerty123456", "qwerty1234567890123",
    "letmein1234567", "1234567890qwertyuiop123", "qwerty123456789012345", "password123456789012",
    "1234567890qwertyuiop123456", "qwerty1234567890123456", "letmein12345678901",
    "1234567890qwertyuiop1234567", "qwerty12345678901234567", "password12345678901234",
    "1234567890qwertyuiop123456789", "qwerty123456789012345678", "letmein123456789012",
    "1234567890qwertyui","name@214230","231123@23111","#234ajlawer234","wwerlaf;werpoiu47987&*(#$)","342709$6ekwjrq#",
    "Ami Tomar Jan","youaremine","iamyours"
])
    

# A set of common leet speak substitutions
LEET_SPEAK_SUBSTITUTIONS = {
    'a': '4', 'b': '8', 'e': '3', 'g': '9', 'i': '1', 'o': '0', 's': '5', 't': '7'
}

def check_length(password):
    return len(password) >= 12

def check_complexity(password):
    return (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def check_common_patterns(password):
    return password not in COMMON_PASSWORDS

def check_leet_speak(password):
    for char, leet in LEET_SPEAK_SUBSTITUTIONS.items():
        if leet in password:
            return False
    return True

def check_repeated_characters(password):
    return not re.search(r'(.)\1{2,}', password)  # No character should repeat 3 or more times

def check_sequential_characters(password):
    sequences = [''.join(chr(i) for i in range(start, start + length)) for start in range(97, 123) for length in range(3, 6)]
    sequences += [''.join(chr(i) for i in range(start, start + length)) for start in range(65, 91) for length in range(3, 6)]
    sequences += [''.join(str(i) for i in range(start, start + length)) for start in range(10) for length in range(3, 6)]
    return not any(seq in password for seq in sequences)

def calculate_entropy(password):
    if len(password) == 0:
        return 0
    frequency = Counter(password)
    probabilities = [freq / len(password) for freq in frequency.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy

def calculate_character_set_entropy(password):
    unique_characters = len(set(password))
    return len(password) * math.log2(unique_characters) if unique_characters > 0 else 0

def password_strength_checker(password):
    length_check = check_length(password)
    complexity_check = check_complexity(password)
    common_patterns_check = check_common_patterns(password)
    leet_speak_check = check_leet_speak(password)
    repeated_characters_check = check_repeated_characters(password)
    sequential_characters_check = check_sequential_characters(password)
    entropy = calculate_entropy(password)
    character_set_entropy = calculate_character_set_entropy(password)

    print(f"\n->Length Check: {length_check}")
    print(f"->Complexity Check: {complexity_check}")
    print(f"->Common Patterns Check: {common_patterns_check}")
    print(f"->Leet Speak Check: {leet_speak_check}")
    print(f"->Repeated Characters Check: {repeated_characters_check}")
    print(f"->Sequential Characters Check: {sequential_characters_check}")
    print(f"->Entropy: {entropy}")
    print(f"->Character Set Entropy: {character_set_entropy}")

    strength = 0
    feedback = []

    if length_check:
        strength += 1
    else:
        feedback.append("->Password should be at least 12 characters long.")

    if complexity_check:
        strength += 1
    else:
        feedback.append("->Password should include uppercase, lowercase, numbers & special characters<-")

    if common_patterns_check:
        strength += 1
    else:
        feedback.append("->Password is too common or easily guessable.")

    if leet_speak_check:
        strength += 1
    else:
        feedback.append("->Avoid using common leet speak substitutions.")

    if repeated_characters_check:
        strength += 1
    else:
        feedback.append("->Avoid using the same character more than twice in a row.")

    if sequential_characters_check:
        strength += 1
    else:
        feedback.append("->Avoid using sequences of characters (e.g., 'abc', '123').")

    if entropy > 40:  # Arbitrary threshold for high entropy
        strength += 1

    print(f"->Strength Score: {strength}\n")

    if strength == 6:
        return "Strong", feedback
    elif strength >= 4:
        return "Medium", feedback
    elif strength == 2:
        return "Weak", feedback
    else:
        return "Very Weak", feedback

def check_password_breach(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    try:
        response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}', timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"->Error checking password breach: {e}")
        return None  # Or handle it in a way that makes sense for your application

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h.lower() == suffix.lower():
            return True  # Password has been breached
    return False  # Password is safe

def generate_strong_password(length=16):
    # Generate a strong password
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage
if __name__ == "__main__":
    password = input("-->>Enter A Password To Check It's Strength: ")
    
    # Check password strength
    strength, feedback = password_strength_checker(password)
    print(f"-->>The password '{password}' is {strength}.\n")
    for message in feedback:
        print(message)

    # Check if the password has been breached
    if check_password_breach(password):
        print("\n-->This Password Has Been Breached! Consider Using A Different Password<-")
        # Suggest a strong password
        strong_password = generate_strong_password()
        print(f"->Suggested strong password: {strong_password}")
    else:
        print("-->This Password Has Not Been Breached<--")
