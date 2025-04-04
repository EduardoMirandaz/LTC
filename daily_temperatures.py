class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        n = len(temperatures)
        ans = [0] * n

        for i in range(n-1, -1, -1):
            current_temperature = temperatures[i]
            
            if not stack:
                stack.append(i)
                ans[i] = 0
            else:
                while stack and current_temperature >= temperatures[stack[-1]]:
                    stack.pop()
                else:
                    if stack:
                        ans[i] = abs(i - stack[-1])
                    else:
                        ans[i] = 0
                    stack.append(i)
        return ans