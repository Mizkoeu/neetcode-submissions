class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        count = 0
        def dfs(grid, r, c, m, n):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for x, y in dirs:
                if r+x>=0 and r+x<m and c+y>=0 and c+y<n:
                    dfs(grid, r+x, c+y, m, n)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c, m, n)
        return count

