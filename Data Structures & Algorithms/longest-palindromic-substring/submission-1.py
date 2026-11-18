class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, maxLen = 0, 0
        
        def expand(l: int, r: int):
            nonlocal start, maxLen
            while l>=0 and r<n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    start = l

                l -= 1
                r += 1

        for i in range(n):
            expand(i,i)
            expand(i,i+1)

        return s[start: start + maxLen]
        