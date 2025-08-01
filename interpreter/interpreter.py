def main()
    expresion = input("Expression)
    x_str, operator, z_str = expression.split(" ")

    x = int(x_str)
    y = int(z_str)

if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z
    else:
        print("Invalid operator")
        return

    print(f"{result:.1f}")

main()




