class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        sum = 0
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                sum-=num
            else:
                seen.add(num)
                sum+=num

        return sum
    

## A better solution is to use XOR operator:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for num in nums:
            res = res ^ num 
        return res
