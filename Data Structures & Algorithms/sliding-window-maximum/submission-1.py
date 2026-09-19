from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        if len(nums) < k:
            return res

        window = deque()
        max_q = deque()

        for right in range(len(nums)):
            window.append(nums[right])

            while max_q and max_q[-1] < nums[right]:
                max_q.pop()
            max_q.append(nums[right])

            if len(window) == k:
                res.append(max_q[0])
                left = window.popleft()
                if left == max_q[0]:
                    max_q.popleft()

        return res
        