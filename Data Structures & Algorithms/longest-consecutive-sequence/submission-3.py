class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cnt = 0

        nums_sets = set(nums)
        unique_start = set()
        for num in nums_sets:
            if num - 1 not in nums_sets:
                unique_start.add(num)

    
        for num in unique_start:
            cnt = 1
            while num + 1 in nums_sets:
                cnt += 1
                num += 1

            max_cnt = max(max_cnt, cnt)

        return max_cnt