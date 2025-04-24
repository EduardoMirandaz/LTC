# monotonic stack

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0

        for price in prices:
            if not stack:
                stack.append(price)
            else:
                while(stack and price < stack[-1]):
                    max_profit = max(max_profit, abs(stack[0] - stack[-1]))
                    stack.pop()

                stack.append(price)

        return max(max_profit, abs(stack[0] - stack[-1]))
    

# two pointers


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 0
        
        max_profit = 0

        arr_length = len(prices)
        
        while right < arr_length:

            profit = prices[right] - prices[left]
            
            
            if(profit <= 0):
                left = right           
            else:
                max_profit = max(max_profit, profit)

            right += 1

            
        return max_profit


