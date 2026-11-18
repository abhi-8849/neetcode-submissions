class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robLine(houses):
            prev, curr = 0, 0
            for h in houses:
                prev, curr = curr, max(curr, prev + h)
            
            return curr

        return max(robLine(nums[:-1]), robLine(nums[1:]))
        