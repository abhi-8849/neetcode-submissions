class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            hl = heights[left]
            hr = heights[right]
            height = min(hl, hr)
            max_area = max(max_area, (right - left) * height)
            if hl <= hr:
                left += 1
            elif hl > hr:
                right -= 1

        return max_area
        