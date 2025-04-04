class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        n = len(heights)
        
        for i in range(n):
            start = i
            while (stack and heights[i] < stack[-1]):
                unstacked_height, unstacked_index = stack.pop(), stack.pop()
                max_area = max(max_area, unstacked_height * (i-unstacked_index))
                start = unstacked_index
            stack.append(start)
            stack.append(heights[i])
        while (stack):
            unstacked_height, unstacked_index = stack.pop(), stack.pop()
            max_area = max(max_area, unstacked_height * (n-unstacked_index))

        return max_area
                