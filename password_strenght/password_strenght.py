def main():
    password = input("Password: ")
    if is_strong(password):
        print("Strong")
    else:
        print("Weak")

def is_strong(s):
    # Step 1: Check length (>= 8)
    if len(s) < 8:
        return False

    # Step 2: Check for at least one uppercase letter
    if not any(char.isupper() for char in s):
        return False

    # Step 3: Check for at least one lowercase letter
    if not any(char.islower() for char in s):
        return False

    # Step 4: Check for at least one digit
    if not any(char.isdigit() for char in s):
        return False

    # Step 5: Check for at least one special character from !@#$%
    special_chars = "!@#$%"
    if not any(char in special_chars for char in s):
        return False

    # Step 6: Check for no spaces
    if " " in s:  # Simpler than a loop
        return False

    # If all checks pass, the password is strong
    return True

if __name__ == "__main__":
    main()
