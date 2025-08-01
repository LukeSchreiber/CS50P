# plates.py

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Rule 1: Length must be between 2 and 6 characters
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Rule 2: Must start with at least two letters
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    # Rule 3: No punctuation, spaces, or special characters
    for char in plate:
        if not char.isalnum():  # not a letter or digit
            return False

    # Rule 4 + 5: Numbers must be at the end, and can't start with 0
    number_started = False  # tracks if we've started seeing digits
    for char in plate:
        if char.isdigit():
            if not number_started and char == '0':
                return False  # first number can't be 0
            number_started = True
        elif number_started and char.isalpha():
            return False  # can't have letters after numbers start

    # All checks passed
    return True


# Only runs main() if this file is executed directly
if __name__ == "__main__":
    main()
