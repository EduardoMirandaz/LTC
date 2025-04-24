class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        left, right = 0, k

        actual_sum = sum(nums[:k])

        avg = actual_sum / k
        higher_avg = avg
        
        while right < n:

            actual_sum = actual_sum - nums[left] + nums[right]
            avg =  actual_sum / k

            higher_avg = max(higher_avg, avg)

            left+=1
            right+=1

        return higher_avg