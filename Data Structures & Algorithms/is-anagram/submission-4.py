class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = [0]*26
        for c in s:
            d[ord(c) - ord('a')] += 1

        for c in t:
            idx = ord(c) - ord('a')
            if d[idx] == 0:
                return False
            d[idx] -= 1
        return True
        