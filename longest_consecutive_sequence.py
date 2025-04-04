class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        longest_consecutive_size = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                acc = 1            
                while num + acc in set_nums:
                    acc += 1
                longest_consecutive_size = max(longest_consecutive_size, acc)
        
        return longest_consecutive_size