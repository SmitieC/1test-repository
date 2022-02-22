def print_word(word, number):
    word, number = input("Enter a word: "), int(input("Enter a number: "))
    print(word.lower()[:number].upper() + word.lower()[number:])


print_word(print_word, print_word)
