from collections import defaultdict

class Solution:
    def isSorted(self, lst: list[int]):
        for i in range(len(lst)-1):
            if(lst[i+1] < lst[i]):
                return False
        return True
    
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        sums = defaultdict(list)

        candidates.sort()

        for i in range(len(candidates)):
            for j in range(len(candidates)):
                if(i != j and candidates[i] + candidates[j] < target):
                    s = candidates[i] + candidates[j]
                    # l = sorted([candidates[i], candidates[j]])
                    sums[s].append([candidates[i], candidates[j]])

                if(i != j and candidates[i] + candidates[j] == target):
                    s = candidates[i] + candidates[j]
                    sums[s].append([candidates[i], candidates[j]])

        for num in candidates:
            tmp = [num]
            while sum(tmp) < target:
                sums[sum(tmp)].append(tmp[:])
                tmp.append(num)

            if sum(tmp) == target: 
                sums[target].append(tmp)

            if (target - num) in sums:
                for lst in sums[target-num]:
                    tmp_list = lst[:]
                    tmp_list.append(num)
                    sums[target].append(tmp_list)
        
        result = []
        seen = set()

        for lst in sums[target]:
            sorted_lst = tuple(sorted(lst))
            if sorted_lst not in seen:
                seen.add(sorted_lst)
                result.append(sorted_lst)

        return result
# possibilities -> 1
# 5, 7
# 2, 4, 6, 8
# 3, 
if __name__ == '__main__':
    c = Solution()
    print(c.combinationSum([7,3,2], 18))

