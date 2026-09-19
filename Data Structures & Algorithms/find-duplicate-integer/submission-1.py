from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        last_seen = defaultdict(int)
        for num in nums:
            if num in last_seen:
                return num
            last_seen[num] += 1
        return num
