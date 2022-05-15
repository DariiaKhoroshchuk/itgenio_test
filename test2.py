def minimum(numbers):
    rows_sum = list()
    columns_sum = list()
    index = list()
    for i in range(len(numbers)):
        rows_sum.append(sum(numbers[i]))
    rows_min_sum = min(rows_sum)
    index.insert(0, rows_sum.index(rows_min_sum))

    for n in range(len(numbers)):  # 0, 1
        column_sum = 0
        for i in range(len(numbers)):
            column_sum += numbers[i][n]
        columns_sum.append(column_sum)
    columns_min_sum = min(columns_sum)
    index.insert(1, columns_sum.index(columns_min_sum))
    return index


print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))
print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))
