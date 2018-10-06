'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

def number_of_island(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    count = 0

    def expand_from(r, c):
        matrix[r][c] = "0"
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in direction:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == "1":
                expand_from(nr, nc)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                expand_from(i, j)
                count += 1
    return count

print(number_of_island([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))