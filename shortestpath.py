from collections import deque

def sort_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    arr = [matrix[i][j] for i in range(m) for j in range(n)]
    arr.sort()
    sorted_matrix = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            sorted_matrix[i][j] = arr[i*n + j]
    return sorted_matrix


def shortest_path(matrix, start_row, start_col, target_row, target_col):
    m, n = len(matrix), len(matrix[0])
    queue = deque([(start_row, start_col, 0)])
    visited = [[False for j in range(n)] for i in range(m)]
    visited[start_row][start_col] = True
    while queue:
        row, col, dist = queue.popleft()
        if row == target_row and col == target_col:
            return dist
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col]:
                queue.append((new_row, new_col, dist + 1))
                visited[new_row][new_col] = True
    return -1


matrix = [[5, 7, 3, 2], [1, 9, 8, 4], [6, 0, 3, 1]]
sorted_matrix = sort_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nSorted Matrix:")
for row in sorted_matrix:
    print(row)

start_row, start_col = 0, 0
target_row, target_col = 2, 3
shortest_dist = shortest_path(matrix, start_row, start_col, target_row, target_col)
print(f"\nShortest path from ({start_row}, {start_col}) to ({target_row}, {target_col}): {shortest_dist}")
