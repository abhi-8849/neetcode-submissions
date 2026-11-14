class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(start: int, left: int) -> None:
            if left == 0:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if left < nums[i]:
                    break

                path.append(nums[i])
                dfs(i, left - nums[i])
                path.pop()

        dfs(0, target)
        return res
        