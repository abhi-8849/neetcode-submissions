from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = Counter(t)
        need = len(target)

        window = defaultdict(int)
        have = 0

        left = 0
        min_len = float('inf')
        min_start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in target and window[char] == target[char]:
                have += 1

            while left <= right and have == need:
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    min_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1

                left += 1
            
        return s[min_start: min_start + min_len] if min_len != float('inf') else ""