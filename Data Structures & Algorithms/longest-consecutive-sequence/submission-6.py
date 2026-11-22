class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nos = set(nums)
        longest = 0

        for num in nos:
            if num - 1 not in nos:
                cnt = 1
                while num + cnt in  nos:
                    cnt += 1
                
                longest = max(longest, cnt)

        return longest