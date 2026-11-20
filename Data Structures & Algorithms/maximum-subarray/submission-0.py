class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = sum = nums[0]

        for x in nums[1:]:
            sum = max(x, sum + x)
            best = max(best, sum)

        return best
        