#увеличить значения в списке в 2 раза
ls = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print("Before:", ls)

# for item in ls:
#     item *=2
for index in range(len(ls)):
    ls[index] *= 2

print("After:", ls)
