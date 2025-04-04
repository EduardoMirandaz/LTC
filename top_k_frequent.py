
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for num in nums:
            if(num in map):
                map[num] += 1
            else:
                map[num] = 1
        
        heap = [(value, key) for key, value in map.items()]
        
        heapq.heapify(heap)
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
