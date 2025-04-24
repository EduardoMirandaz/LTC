class Solution:


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr_length = len(nums)
        
        seen = {}

        for i in range(arr_length):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i



# other solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {
            target-nums[0] : 0
        }

        n = len(nums)

        for i in range(1,n):
            
            if(nums[i] in diffs):
                return diffs[nums[i]], i

            diffs[target-nums[i]] = i