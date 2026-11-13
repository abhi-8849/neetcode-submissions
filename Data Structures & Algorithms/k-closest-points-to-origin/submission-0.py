import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dis = x*x + y*y
            heapq.heappush_max(heap, (dis, x, y))

            if len(heap) > k:
                heapq.heappop_max(heap)

        return [[x,y] for _,x,y in heap]