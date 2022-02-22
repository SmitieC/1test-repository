def find_longest_word(string_list):
    longest_word = ""
    for word in string_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


# main
string_list = input("Enter a list of words: ").split()
print(string_list)
print(find_longest_word(string_list))
