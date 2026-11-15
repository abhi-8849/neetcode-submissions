import sys
sys.setrecursionlimit(100000)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        visited = set()

        def dfs(r, c, group):

            if (r < 0 or r >= R or c < 0 or c >= C or board[r][c] != 'O'
                or (r,c) in visited):
                return

            visited.add((r,c))
            group["cells"].append((r,c))

            if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                group["edge"] = True

            dfs(r+1, c, group)
            dfs(r-1, c, group)
            dfs(r, c-1, group)
            dfs(r, c+1, group)
        
        for r in range(R):
            for c in range(C):
                group = {"cells": [], "edge": False}

                if board[r][c] == 'O' and (r,c) not in visited:
                    dfs(r, c, group)

                    if not group["edge"]:
                        for gr, gc in group["cells"]:
                            board[gr][gc] = 'X'
        