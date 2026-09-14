class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                prod *= num

        if zeros > 1:
            return [0] * len(nums)

        result = []
        for num in nums:
            if zeros == 1:
                result.append(prod if num == 0 else 0)
            else:
                result.append(prod//num)

        return result