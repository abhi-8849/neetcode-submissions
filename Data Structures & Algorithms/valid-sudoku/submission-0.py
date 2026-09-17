from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                grid_id = (r//3, c//3)

                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[grid_id]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[grid_id].add(val)

        return True