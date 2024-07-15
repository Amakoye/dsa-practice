def pascalTriangle(numRows):
    if numRows <= 0:
        return []

    init_triangle = [[1]]

    for i in range(1, numRows):
        previous_row = init_triangle[i - 1]

        new_row = [1]

        for j in range(1, i):
            new_row.append(previous_row[j - 1] + previous_row[j])
        new_row.append(1)

        init_triangle.append(new_row)

    return init_triangle


print(pascalTriangle(numRows=5))
