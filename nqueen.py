def is_safe(arr, x, y, n):
    # Check if placing a queen at position (x, y) is safe
    for row in range(x):
        if arr[row][y] == 1:
            return False

    row, col = x, y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row, col = x, y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True

def n_queen(arr, x, n):
    if x >= n:
        return True

    for col in range(n):
        if is_safe(arr, x, col, n):
            arr[x][col] = 1
            if n_queen(arr, x + 1, n):
                return True
            arr[x][col] = 0

    return False

def print_solution(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()

n = int(input("Enter the value of N: "))
print()
arr = [[0 for _ in range(n)] for _ in range(n)]

if n_queen(arr, 0, n):
    print_solution(arr, n)
else:
    print("No solution exists for N =", n)

