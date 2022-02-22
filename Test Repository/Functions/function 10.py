def longest_word(string_list):
    longest = ""
    for word in string_list:
        if len(word) > len(longest):
            longest = word
    print(longest)


# main
string_list = []
while string_list[-1] != "x":
    string_list.append(input("Enter a word: "))
else:
    longest_word(string_list)
