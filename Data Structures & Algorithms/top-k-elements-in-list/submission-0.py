from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = Counter(nums).most_common(k)
        return [item[0] for item in top_k]
        
        