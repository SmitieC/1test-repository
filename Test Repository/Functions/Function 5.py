def factor(num1, num2):
    if num1 % num2 == 0:
        print(f"Yes {num2}is a factor of {num1}")
    else:
        print(f"No {num2} is not a factor of {num1}")

#main
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
factor(num1, num2)
