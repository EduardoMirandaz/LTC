class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height)-1

        max_area = 0

        while left < right:

            minor = min(height[left], height[right])

            area = minor * (right - left)

            max_area = max(max_area, area)


            if minor == height[left]:
                left += 1
            else:
                right -= 1

        return max_area
