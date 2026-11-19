class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        
        while left < right:
            k = left + (right - left) // 2

            if self.can_finish(piles, k, h):
                right = k
            else:
                left = k + 1

        return left

    def can_finish(self, piles: List[int], k: int, h: int) -> bool:
        cnt = 0
        for pile in piles:
            cnt += (pile // k)
            if pile % k:
                cnt += 1

        return cnt <= h