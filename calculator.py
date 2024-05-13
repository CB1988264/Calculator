classmethod# This function adds two numbers
import math

def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def sin (x):
    return math.sin(x)

def cos (x):
    return math.cos(x)

def numberGetter():
    try:
        number = int(input("Give a number: "))
        return number
    except (TypeError, ValueError):
        print('This input is invalid.')
        return numberGetter()


def options():
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(number1/number2)")
    print("(6) cos(number1/number2)")
    print("(7) Change numbers")
    print("(8) Quit")

def start():
    print("Calculator")

    num1 = numberGetter()
    num2 = numberGetter()



    while True:
        options()
        print("Current numbers:", num1, num2)
        selection = input("Please select something (1-6): ")
        if selection == '8':
            print("Thank you!")
            break
        elif selection == '1':
            print("The result is: ", + add(num1, num2))
        elif selection == '2':
            print("The result is: ", + subtract(num1, num2))
        elif selection == '3':
            print("The result is: ", + multiply(num1, num2))
        elif selection == '4':
            print("The result is: ", + divide(num1, num2))
        elif selection == '5':
            print("The result is: ", + sin(num1/num2))
        elif selection == '6':
            print("The result is: ", + cos(num1/num2))
        elif selection == '7':
            num1 = int(input("give the first number: "))
            num2 = int(input("give the second number: "))

def main():
    start()

if __name__ == "__main__":
    main()