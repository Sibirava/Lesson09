def calculate_average_marks(marks):
    s = 0

    for element in marks:
        s += element
    return s / len(marks)


# def main ():
#     mark1 = int(input("Input  mark1: "))
#     mark2 = int(input("Input  mark2: "))
#     mark3 = int(input("Input  mark3: "))
#
#     avg = calculate_average_marks(mark1, mark2, mark3)
#     msg = f"Students' average mark is: {round(avg, 2)}"
#     print(msg)
#
# main()


def main():
    marks = []

    mark = 0

    print("Input student's marks.\n for exit input -1\n")
    while mark != -1:
        mark = int(input("input mark: "))
        marks.append(mark)

    marks.remove(-1)

    # if mark !=-1:
    #     marks.append(mark)
    # print("Your marks:" +str(marks))+
    avg = calculate_average_marks(marks)

    msg = f"Average of students' marks is {avg}"

    print(msg)


main()
