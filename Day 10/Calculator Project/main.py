import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)

    num_1 = float(input("Enter the first number: "))

    while True:
        for symbol in operation:
            print(symbol)

        operator = input("Enter the operator: ")
        num_2 = float(input("Enter the second number: "))

        answer = operation[operator](num_1, num_2)

        print(f"{num_1} {operator} {num_2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or 'n' to start over: ").lower()

        if choice == "y":
            num_1 = answer
        else:
            print("\n" * 20)
            calculator()


calculator()