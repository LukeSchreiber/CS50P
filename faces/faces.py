def convert(text):
    # Swap :) for the smiling emoji (🙂)
    text = text.replace(":)", "🙂")
    # Swap :( for the frowning emoji (🙁)
    text = text.replace(":(", "🙁")
    # Return the updated string
    return text

def main():
    # Here's where user input happens! Prompt and get the string
    user_text = input("Enter your text (try including :) or :()): ")
    # Call convert with the user's input
    converted = convert(user_text)
    # Print the result
    print(converted)

# Call main to start the program (this runs when you execute the file)
if __name__ == "__main__":
    main()
