class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid is greater than the rightmost element, 
            # the pivot/minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is in the left half, and could be mid itself.
            else:
                right = mid
                
        # When left == right, we've found the minimum element
        return nums[left]