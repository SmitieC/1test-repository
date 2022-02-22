def check_a(word):
    if word[0].lower() == 'a':
        return True
    else:
        return False


# main
if check_a(word = input("Enter a word: ")) == False:
    print("The word doesn't start with a")
else:
    print("The word starts with a")
