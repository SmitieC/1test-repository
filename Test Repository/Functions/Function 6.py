def numbers_in_list(list, multiple):
    new_list = []
    for i in list:
        if i % multiple == 0:
            new_list.append(i)
    return new_list

print(numbers_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
