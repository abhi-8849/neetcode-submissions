from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def f(i: int) -> int:
            if i <= 1:
                return 1

            return f(i-1) + f(i-2)

        return f(n)