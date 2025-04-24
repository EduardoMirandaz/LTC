class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        right_index = n-1
        left_index = 0
        
        while True:
            res = numbers[left_index] + numbers[right_index]
            
            if( res == target ):
                return [left_index+1,right_index+1]
            elif( res < target ):
                left_index+=1
            else:
                right_index-=1