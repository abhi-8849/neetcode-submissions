from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i, num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    del d
                    return True
            
            d[num] = i
        del d
        return False
        