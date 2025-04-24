class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        prefix_sum_map = {0:1}

        acc = 0
        
        for num in nums:
            acc += num        
            
            res += prefix_sum_map.get(acc - k, 0)
            prefix_sum_map[acc] = prefix_sum_map.get(acc, 0) + 1

        return res