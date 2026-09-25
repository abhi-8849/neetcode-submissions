import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            
            # Calculate total hours needed at eating speed 'k'
            hours = sum(math.ceil(p / k) for p in piles)
            
            if hours <= h:
                res = k
                right = k - 1  # Speed works, but check if we can eat even slower
            else:
                left = k + 1   # Too slow, must increase speed
                
        return res