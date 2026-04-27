def add(a,b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def devide(a, b):
    if b == 0:
         return "Cannot divide by zero"
    return a / b

while True:
    print("\nCalculator")
    print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")

    choice = input("Which operation you want to perform add your choice : ")

    if choice == '5':
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", sub(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", devide(a, b))
    else:
        print("Invalid choice")
