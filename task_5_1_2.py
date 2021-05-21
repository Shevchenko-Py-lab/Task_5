from itertools import islice

nums_gen = (num for num in range(1, 15 + 1, 2))
print(*nums_gen)


def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
print(*islice((odd_to_15), 8))
print(next(odd_to_15))

