class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0 
        highest_sum = nums[0]
        for num in nums:
            curr_sum += num

            if(num > curr_sum):
                curr_sum = num
            
            highest_sum = max(curr_sum, highest_sum)
        
        return highest_sum
    
