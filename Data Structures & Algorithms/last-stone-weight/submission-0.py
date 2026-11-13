import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)

        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)

            if s1 != s2:
                heapq.heappush_max(stones, s1-s2)

        return stones[0] if len(stones) == 1 else 0