class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_left = 1
        prod_left_list = [1]
        for i in range(1, len(nums)):
            prod_left *= nums[i-1]
            prod_left_list.append(prod_left)

        prod_right = 1
        prod_right_list = [1]
        for i in range(len(nums)-1, 0, -1):
            prod_right *= nums[i]
            prod_right_list.append(prod_right)

        pr = list(reversed(prod_right_list))

        result = []
        for i in range(len(nums)):
            ans = prod_left_list[i]*pr[i]
            result.append(ans)

        return result

        