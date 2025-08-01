def main():
    word = input("Word: ")
    result = word_score(word)
    print(result)

def word_score(s):
    # Check if the input contains only letters
    if not s.isalpha():
        return "Invalid"

    # Define dictionary for vowel points (1 point each)
    points = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

    # Initialize score
    score = 0

    # Loop through each character in lowercase
    for char in s.lower():
        # If character is a vowel (in dictionary), add its points
        if char in points:
            score += points[char]
        # If character is a consonant (not in dictionary), add 2 points
        else:
            score += 2

    return score

if __name__ == "__main__":
    main()
