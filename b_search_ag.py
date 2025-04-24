class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while(left <= right):

            middle_index = (left+right)//2

            if(target > nums[middle_index]):
                left = middle_index+1
            elif(target < nums[middle_index]):
                right = middle_index-1
            else:
                return middle_index

        return -1
