class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort()

        for interval in intervals:
            
            if len(ans) == 0:
                ans.append([interval[0], interval[1]])
            else:
                if(interval[0] <= ans[-1][1]):
                    ans[-1][1] = max(interval[1], ans[-1][1]) 
                    if(interval[0] < ans[-1][0]):
                        ans[-1][0] = interval[0]
                else:
                    ans.append([interval[0], interval[1]])
        return ans