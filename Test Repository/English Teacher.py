student_list = []  # List of students
mark_list = []  # List of marks
while True:
    student_name = input("Enter the name of the student: ")
    if student_name == "X":
        break
    student_list.append([student_name])
    mark = int(input("Enter the mark of the student: "))
    mark_list.append(mark)

print("The average mark is:", (sum(mark_list) / len(mark_list)))
# get average mark by summing all grades and dividing by number of students
print("The best mark is:", max(mark_list))
# get best mark by finding the highest grade by using max boolean expression


# number 6

while len(student_list) > 0:
    if mark_list[0] < 40:
        print(student_list[0][0], "has an E")
    elif mark_list[0] < 50:
        print(student_list[0][0], "has a D")
    elif mark_list[0] < 55:
        print(student_list[0][0], "has a C-")
    elif mark_list[0] < 60:
        print(student_list[0][0], "has a C")
    elif mark_list[0] < 65:
        print(student_list[0][0], "has a C+")
    elif mark_list[0] < 70:
        print(student_list[0][0], "has a B-")
    elif mark_list[0] < 75:
        print(student_list[0][0], "has a B")
    elif mark_list[0] < 80:
        print(student_list[0][0], "has a B+")
    elif mark_list[0] < 85:
        print(student_list[0][0], "has an A-")
    elif mark_list[0] < 90:
        print(student_list[0][0], "has an A")
    else:
        print(student_list[0][0], "has an A+")
    student_list.pop(0)
    mark_list.pop(0)
