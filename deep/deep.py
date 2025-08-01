user_input = input("What is the answer to the universe and everything? ").strip()  # Strip spaces

if user_input in ("42", "Forty-two", "forty-two"):  # Check any match
    print("Correct")
else:
    print("not correct")
