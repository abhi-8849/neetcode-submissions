class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]

        prod_left = 1
        for i in range(1, len(nums)):
            prod_left *= nums[i-1]
            result.append(prod_left)

        prod_right = 1
        for i in range(len(nums)-1, 0, -1):
            prod_right *= nums[i]
            result[i-1] *= prod_right

        return result

        