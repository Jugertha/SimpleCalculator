import math 
print ("hello world!")
print ("This is a pyhton calculator")
print ("This calculator can perform basic arithmetic operations like addition, subtraction, multiplication, and division.")
numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
print ("Select operation:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
choice = input("Enter choice (1/2/3/4): ")
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
else:
    print ("Invalid input") 
    