nums_gen = (num for num in range(1, 15 + 1, 2))
print(*nums_gen)


def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
print(next(odd_to_15))  # 1
print(next(odd_to_15))  # 3
print(next(odd_to_15))  # 5
print(next(odd_to_15))  # 7
print(next(odd_to_15))  # 9
print(next(odd_to_15))  # 11
print(next(odd_to_15))  # 13
print(next(odd_to_15))  # 15
print(next(odd_to_15))  # StopIteration
