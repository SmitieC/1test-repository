def main():
    sales = 0
    adult = 0
    student = 0
    child = 0
    gift = 0
    while True:
        input_again = input("Would you like to sell a ticket:\ny for yes and n"
                            " for no: ")
        if input_again == "y":

            print("a for adult, s for student, c for child, g for gift card")
            print("Enter n to quit")
            ticket = input("Enter the type of ticket sold: ")
            if ticket == "n":
                break

            if ticket == "a":
                adult += 1
                sales += 1
            elif ticket == "s":
                student += 1
                sales += 1
            elif ticket == "c":
                child += 1
                sales += 1
            elif ticket == "g":
                gift += 1
                sales += 1
            else:
                print("Invalid entry")
        elif input_again == "n":
            print("Total sales: ", sales)
            print("Adult tickets sold: ", adult)
            print("Student tickets sold: ", student)
            print("Child tickets sold: ", child)
            print("Gift card tickets sold: ", gift)
            break


# main
main()
