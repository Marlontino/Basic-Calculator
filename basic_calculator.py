#Interface for program
while True:
    print("Options:")
    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

#Logic for expressions
    if user_input == "quit":
        break
    elif user_input == "+":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "-":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
    elif user_input == "*":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
    elif user_input == "/":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
    else:
        print("Unknown input")
