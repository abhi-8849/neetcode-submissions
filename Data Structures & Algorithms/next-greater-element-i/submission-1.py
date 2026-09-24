class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                d[nums2[stack.pop()]] = nums2[i]
            stack.append(i)

        return [d.get(num, -1) for num in nums1]

        