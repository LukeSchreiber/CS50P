import pyfiglet
import sys

def main():
    # Get text and font from command-line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python figlet.py 'text' [font]")
        sys.exit(1)

    user_text = sys.argv[1]
    user_font = sys.argv[2] if len(sys.argv) == 3 else "standard"

    # Check if the input is valid (e.g., not empty)
    if not user_text:
        print("You didn't enter any text")
        sys.exit(1)

    # Create the ASCII art and display it
    result = pyfiglet.Figlet(font=user_font).renderText(user_text)
    print(result)

if __name__ == "__main__":
    main()
