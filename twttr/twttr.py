# twttr.py: Remove vowels from user input string
def remove_vowels(text):
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    result = ""  # Initialize empty string to build output
    for char in text:  # Iterate through each character
        if char not in vowels:  # Keep non-vowel characters
            result += char
    return result

# Main program
def main():
    # Prompt user for input
    text = input("Input: ")
    # Remove vowels and get result
    result = remove_vowels(text)
    # Print the result
    print("Output:", result)

# Run the program
if __name__ == "__main__":
    main()
