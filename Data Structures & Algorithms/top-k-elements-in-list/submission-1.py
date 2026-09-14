from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        freq_buckets = []
        for _ in range(len(nums) + 1):
            freq_buckets.append([])

        for num, freq in d.items():
            freq_buckets[freq].append(num)

        result = []
        for i in range(len(freq_buckets) - 1, -1, -1):
            for num in freq_buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        

        
        