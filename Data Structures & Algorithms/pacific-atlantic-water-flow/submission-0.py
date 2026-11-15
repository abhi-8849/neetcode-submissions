class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, seen):
            seen.add((r,c))

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (0 <= nr < R and 0 <= nc < C
                    and (nr, nc) not in seen
                    and heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr,nc, seen)

        pac, atl = set(), set()

        for r in range(R):
            dfs(r, 0, pac)
            dfs(r, C-1, atl)

        for c in range(C):
            dfs(0, c, pac)
            dfs(R-1, c, atl)

        return [list(cell) for cell in pac & atl]