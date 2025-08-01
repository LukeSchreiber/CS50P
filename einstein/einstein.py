def formula(mass):
    c = 300000000
    energy = mass * (c ** 2)
    return energy

def main():
    mass = int(input("Enter the mass in kg: "))
    energy = formula(mass)
    print(energy)

if __name__ == "__main__":
    main()
