class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        higher_sequence = 0
        count_1 = 0
        count_0 = 0
        current_accumulator = nums[0]
        while(nums):
            current_value = nums.pop()

            if(current_value == 1):
                if(current_accumulator == 1):
                    count_1 += 1
                else:
                    if(count_1 < count_0 and (count_1+1)*2 > higher_sequence and count_0 == 1):
                        higher_sequence = (count_1+1)*2

                    count_1 = 1
                    current_accumulator = 1
            
            else:
                if(current_accumulator == 0):
                    count_0 += 1
                else:
                    
                    if(count_0 < count_1 and (count_0+1)*2 > higher_sequence and count_0 == 0):
                        higher_sequence = (count_0+1)*2
                    
                    count_0 = 1
                    current_accumulator = 0

            if(count_1 == count_0):
                if(count_0 + count_1 > higher_sequence):
                    higher_sequence = count_0 + count_1
                        
        return higher_sequence