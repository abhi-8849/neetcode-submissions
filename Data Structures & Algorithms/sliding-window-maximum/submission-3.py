from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_q = deque()

        for right in range(len(nums)):
            
            while max_q and nums[max_q[-1]] < nums[right]:
                max_q.pop()
            
            max_q.append(right)

            if max_q[0] < right - k + 1:
                max_q.popleft()

            if right >= k-1:
                res.append(nums[max_q[0]])

        return res
        