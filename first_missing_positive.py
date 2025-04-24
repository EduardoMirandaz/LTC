class Solution:

    def binary_search(self, array, target):
    
        left, right = 0, len(array)-1
        

        while (left <= right):

            mid = (left + right) // 2

            if(array[mid] == target):
                return mid
            elif (target < array[mid]):
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        pos_1 = self.binary_search(nums, 1)

        if pos_1 == -1: return 1
        
        acc = 0
        nums = nums[pos_1:]

        for i in nums:
            acc += 1
            if(i != acc):
                return acc
        else:
            return acc + 1