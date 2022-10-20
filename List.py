# список
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers)
#
# for element in numbers:
#     print(element)

# пустой список
# empty_list = list()
# empty_list = []
#
# numbers = list ("123456789")  # или  (12 34 56 78 9) или (1,2,3,4,5,6,7,8,9)
# print(numbers)

# вывод списка по индексу:
# numbers = [11, 221, 73, 44, 56, 65, 78]
# for index in range(len(numbers)):
    # print(str(index + " - " + str(numbers[index]))
    # print(f"{index} - {numbers[index]}")

# range(a) --> [0...a)
# range(a, b) --> [a..b)
# range(a, b, step) -->[a, a + step, a + 2step, ...b)


# чтобы выводил только четные по индексу
# numbers = [11, 221, 73, 44, 56, 65, 78]
# for index in range(1,len(numbers), 2):
    # print(str(index + " - " + str(numbers[index]))
    # print(f"{index} - {numbers[index]}")



# чтобы выводил только нечетные по индексу
# numbers = [11, 221, 73, 44, 56, 65, 78]
# for index in range(0, len(numbers), 2):
    # print(str(index + " - " + str(numbers[index]))
    # print(f"{index} - {numbers[index]}")





# numbers = [11, 221, 73, 44, 56, 65, 78]
# numbers.append(100)  # в конец списка
# numbers.append(1000)
# print(numbers)

numbers = [11, 221, 73, 44, 56, 65, 78]
numbers.insert(len(numbers), 100)
numbers.insert(len(numbers),1000)
print(numbers)

# в начало списка
numbers = [11, 221, 73, 44, 56, 65, 78]
numbers.insert(0, 100)
numbers.insert(0, 1000)
print(numbers)