#как посчитать количество цифр в числе
def count_number_digits(num):
    count = 0

    while num !=0:
        count += 1
        num //= 10
    return count

def main():
    num = int(input("Input your number: "))
    count = count_number_digits(num)

    msg = f"Number of digits is {count}"
    print(msg)

main()