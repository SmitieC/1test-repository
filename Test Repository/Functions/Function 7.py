def print_name(name, amount):
    name = str(input("What is the name? "))
    amount = int(input("How many times do you want to print the name? "))
    for i in range(amount):
        print(name)


# main
print_name("John", 5)
