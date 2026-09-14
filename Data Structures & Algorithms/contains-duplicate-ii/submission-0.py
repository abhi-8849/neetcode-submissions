from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)

        for i, num in enumerate(nums):
            d[num].append(i)

        for v in d.values():
            if len(v) > 1:
                for j in range(1, len(v)):
                    if v[j] - v[j-1] <= k:
                        return True

        return False