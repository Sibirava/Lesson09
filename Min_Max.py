# экстремальные алгоритмы: макс, мин, среднее арифметическое и среднее геометрическое

def get_max(numbers):
    max = numbers[0]  # доступ к первому элементу

    for element in numbers:
        if element > max:
            max = element

    return max


def get_min(numbers):
    min = numbers[0]  # доступ к первому элементу

    for element in numbers:
        if element < min:
            min = element

    return min


# если надо найти по индексу
def get_last_max_value_index(numbers):
    max_index = 0
    # классический for возвращает только ЗНАЧЕНИЯ!!! он просто перебирает элементы.
    # Надо использовать с range, чтобы вернуть индекс

    for index in range(len(numbers)-1, -1, -1):       # ставим 1, чтобы не сравнивать с самим собой(если перебираем с начала)

        if numbers[index] >= numbers[max_index]:
            max_index = index

    return maх_index


def calc_arithmetical_avg(numbers):
    s = 0
    for num in numbers:
        s += num

    return s / len(numbers)



def calc_geometrical_avg(numbers):
    p = 1
    for num in numbers:
        p *= num

    return p ** (1/ len(numbers))

