import inflect

p = inflect.engine()
names = []

try:
    while True:
        name = input("Enter the name: ")
        names.append(name)
except EOFError:
        print()


formatted_names = p.join(names)
print(f"Adieu, adieu, to {formatted_names}")
