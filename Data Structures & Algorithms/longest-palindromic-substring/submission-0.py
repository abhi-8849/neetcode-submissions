class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        longestSub = ""
        
        def expand(l: int, r: int):
            nonlocal maxLen, longestSub
            while l>=0 and r<n and s[l] == s[r]:
                sub = s[l:r+1]
                if len(sub) > maxLen:
                    maxLen = len(sub)
                    longestSub = sub

                l -= 1
                r += 1

        for i in range(n):
            expand(i,i)
            expand(i,i+1)

        return longestSub
        