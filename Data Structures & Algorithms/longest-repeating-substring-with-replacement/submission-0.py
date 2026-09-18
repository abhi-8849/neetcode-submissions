from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        maxf = 0
        counts = defaultdict(int)


        for right in range(len(s)):
            counts[s[right]] += 1
            maxf = max(maxf, counts[s[right]])

            while (right - left + 1) - maxf > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len    