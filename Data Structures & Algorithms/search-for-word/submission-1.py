class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board), len(board[0])
        starts = []

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    starts.append((r,c))

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r<0 or r>=R or c<0 or c>=C or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'
            found = (dfs(r-1,c,i+1) or
                     dfs(r+1,c,i+1) or
                     dfs(r,c-1,i+1) or
                     dfs(r,c+1,i+1))
            board[r][c] = temp
            return found

        for r,c in starts:
            if dfs(r,c,0):
                return True
        
        return False