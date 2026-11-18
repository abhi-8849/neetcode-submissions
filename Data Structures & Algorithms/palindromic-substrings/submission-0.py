class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0

        def expand(l: int, r: int):
            nonlocal cnt
            while l>=0 and r<n and s[l] == s[r]:
                cnt += 1
                l -=1
                r +=1

        for i in range(n):
            expand(i,i)
            expand(i, i+1)
        
        return cnt