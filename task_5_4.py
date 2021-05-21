src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = set()
for num in range(1, len(src)):
    if src[num] - src[num - 1] > 0:
        result.add(src[num])

result_ord = [el for el in src if el in result]
print(result_ord)
