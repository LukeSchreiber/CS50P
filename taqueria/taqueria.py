menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "torta": 9.00,
    "taco": 3.00,
    "queso": 2.50,
    "carnitas": 7.00
}

def main():
    total = 0.0
    while True:
        try:
            print(f"Total: ${total:.2f}")
            item = input("Item: ").lower().strip()

            if item == "done":
                break

            if item in menu:
                total += menu[item]
            else:
                print("Please enter an item on the menu")

        except KeyError:
            continue
        except ValueError:
            continue

if __name__ == "__main__":
    main()
