class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            j = 31 - i
            if ((n>>i) & 1) != ((n>>j) & 1):
                n ^= (1 << i) | (1 << j)

        return n