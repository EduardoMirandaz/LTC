class Solution:
    def twoSum(self, numbers: list[int], target: int, not_index: int) -> list[int]:
        
        diffs = {}
        
        for i,num in enumerate(numbers):
            
            diff = num - target

            if num in diffs:
                if i != not_index and i != diffs[num] and diffs[num] != not_index:
                    return [numbers[diffs[num]], num]            
            diffs[(diff*-1)] = i
            
        return None

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_array = []

        for i,num in enumerate(nums):
            
            res = self.twoSum(nums, num*-1, i)
            if(res != None):
                res.append(num)
                res.sort()
                if( res not in result_array ):
                    result_array.append( res )
        
        return result_array

