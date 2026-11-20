class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(x):
            total = 0
            while x > 0:
                x, d = divmod(x, 10)
                total += d ** 2
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)

        return n == 1