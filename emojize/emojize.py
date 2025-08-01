
import emoji
import random  # Not used yet, but fine to keep

def main():
    user_input = input("Input: ")  # Use lowercase 'input'
    output = emoji.emojize(user_input)  # Emojize the input
    print("Output:", output)  # Print with label

if __name__ == "__main__":
    main()
