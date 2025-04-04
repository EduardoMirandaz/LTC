class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        ans = []

        intervals.sort(key = lambda i : i[0])

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

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)