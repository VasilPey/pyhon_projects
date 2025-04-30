from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    n1 = float(input("What's the first number?: "))
    should_continue = True
    while should_continue:
        for key in operations:
            print(key)

        user_operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        result = 0
        if user_operation == "+":
            result = operations["+"](n1, n2)
        elif user_operation == "-":
            result = operations["-"](n1, n2)
        elif user_operation == "*":
            result = operations["*"](n1, n2)
        elif user_operation == "/":
            result = operations["/"](n1, n2)

        print(f"{n1} {user_operation} {n2} = {result}")

        continue_or_no = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_or_no == "y":
            n1 = result
        elif (continue_or_no == "n"):
            should_continue = False
            calculator()
calculator()