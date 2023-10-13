def diagonalDifference(arr):
    n = len(arr)
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    for i in range(n):
        left_diagonal_sum += arr[i][i]
        right_diagonal_sum += arr[i][n - i - 1]
    diff = abs(left_diagonal_sum - right_diagonal_sum)
    return diff
matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
result = diagonalDifference(matrix)
print(result)  # Output will be 15
