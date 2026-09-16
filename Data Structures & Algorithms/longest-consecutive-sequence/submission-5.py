class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cnt = 0

        nums_set = set(nums)
        unique_start = set()
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                cnt = 1

                while current_num + 1 in nums_set:
                    cnt += 1
                    current_num += 1

                max_cnt = max(max_cnt, cnt)

        return max_cnt