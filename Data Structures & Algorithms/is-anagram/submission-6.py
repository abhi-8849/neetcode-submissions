from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0]*26
        for c in s:
            index = ord(c) - ord('a')
            cnt[index] += 1

        for c in t:
            index = ord(c) - ord('a')
            if cnt[index] == 0:
                return False
            cnt[index] -= 1

        return True