import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for num in nums:
            d[num] += 1

        heap_data = [(v,k) for k,v in d.items()]
        heapq.heapify_max(heap_data)

        while k:
            res.append(heapq.heappop_max(heap_data)[1])
            k -= 1
            
        return res



 
        

        