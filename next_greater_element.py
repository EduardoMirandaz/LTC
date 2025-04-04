class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        h_map = {}

        n = len(nums2)

        for i in range(n-1, -1, -1):
            if not stack:
                h_map[nums2[i]] = -1
                stack.append(nums2[i])
            else:
                while stack and nums2[i] >= stack[-1]:
                    stack.pop()
                if not stack:
                    h_map[nums2[i]] = -1
                else:
                    h_map[nums2[i]] = stack[-1]
                
                stack.append(nums2[i])

        return [h_map[i] for i in nums1]