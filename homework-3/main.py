from power import Power

if __name__ == "__main__":
    text = "Calculating the power of a number"
    print("~" * len(text) + '\n' + text + "\n" + "~" * len(text) + "\n")
    base = input("Enter the base: ")
    while not base.isdigit():
        base = input("Please enter an integer: ")
    else:
        base = int(base)
    deg = input("Enter the degree: ")
    while not deg.isdigit():
        deg = input("Please enter an integer: ")
    else:
        deg = int(deg)
    print(f"\n{'-' * len(text)}\n{base} ^ {deg} = {Power(base, deg)}")
