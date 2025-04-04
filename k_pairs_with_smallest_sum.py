class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        ans = []
        min_a = 0
        min_b = 0

        len_a = len(nums1)
        len_b = len(nums2)

        while len(ans) < k:
            pair = [min_a, min_b]
            if(pair not in ans):
                ans.append(pair)
                min_a = 0
                min_b = 0

            if(min_a + 1 >= len_a):
                min_b += 1
                continue
            if(min_b + 1 >= len_b):
                min_b += 1
                continue
            
            if(nums1[min_a + 1] - nums1[min_a] > nums2[min_b + 1] - nums2[min_b]):
                min_b+=1
            else:
                min_a+=1
                
        return [ [nums1[pair[0]], nums2[pair[1]] ] for pair in ans]
