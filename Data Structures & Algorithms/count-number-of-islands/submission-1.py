class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        count = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                x, y = q.popleft()
                grid[x][y] = "0"
                for i, j in dirs:
                    if x+i>=0 and x+i<m and y+j>=0 and y+j<n and grid[x+i][y+j]=="1":
                        q.append((x+i,y+j))
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r,c)
        return count

