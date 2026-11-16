from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r,c))

        def fill(r,c,d):
            if 0<=r<R and 0<=c<C and grid[r][c] == INF:
                grid[r][c] = d + 1
                q.append((r,c))

        while q:
            r,c = q.popleft()

            fill(r-1, c, grid[r][c])
            fill(r+1, c, grid[r][c])
            fill(r, c-1, grid[r][c])
            fill(r, c+1, grid[r][c])