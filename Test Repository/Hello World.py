number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

if number1 == number2:
    print("The numbers are equal")
else:
    print("The higher number is: ", max(number1, number2))
