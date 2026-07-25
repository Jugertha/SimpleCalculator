import math 
print ("hello world!")
print ("This is a Python calculator")
print ("This calculator can perform basic arithmetic operations like addition, subtraction, multiplication, and division.")
numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
while True:
    print ("\nSelect operation:")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Power")
    print ("6. new numbers")
    print ("7. Exit")
    choice = input("Enter choice (1/2/3/4/5/6/7/): ")
    if choice == '1': 
        result= numb1 + numb2
        print (f"{numb1} + {numb2} = {result}")
    elif choice == '2':
        result= numb1 - numb2
        print (f"{numb1} - {numb2} = {result}")
    elif choice == '3':
        result= numb1 * numb2
        print (f"{numb1} * {numb2} = {result}")
    elif choice == '4':
        if numb2 != 0:
            result= numb1 / numb2
            print (f"{numb1} / {numb2} = {result}")
        else:
            print ("Error: Division by zero is not allowed.")
    elif choice == '5':
        result= math.pow(numb1, numb2)
        print (f"{numb1} ^ {numb2} = {result}")
    elif choice == '6':
        numb1 = float(input("Enter the first number: "))
        numb2 = float(input("Enter the second number: "))
    elif choice == '7':
        print ("Exiting the calculator. Ciao!")
        break
    else:
        print ("Invalid input") 
    