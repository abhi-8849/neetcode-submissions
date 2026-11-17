from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        fresh = 0
        q = deque()

        for r in range(R):
            for c in range(C):
                
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        mins = 0

        while q and fresh:
            
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            mins += 1

        return mins if fresh == 0 else -1