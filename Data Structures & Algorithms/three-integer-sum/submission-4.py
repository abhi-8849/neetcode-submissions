class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumlr = nums[left] + nums[right]
                sum3 = nums[i] + sumlr
                if sum3 > 0:
                    right -= 1
                elif sum3 < 0:
                    left += 1
                else:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1

        return [ list(triplet) for triplet in triplets]

        
        