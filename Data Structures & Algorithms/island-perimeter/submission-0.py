class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if i not in range(row) or j not in range(col) or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0

            visited.add((i, j))
            perim = dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)

            return perim

        perim = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    perim += dfs(r, c)

        return perim
