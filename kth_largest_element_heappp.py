import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] = -nums[i]

        min_heap = []

        heapq.heapify(nums)

        res = 0
        for _ in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)