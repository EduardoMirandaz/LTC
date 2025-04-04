class Solution:
    def sum_of_squares(self, n: int) -> int:

        mult = 1
        sum = 0
        while n:

            curr_digit = n % (mult*10) // mult
            n -= curr_digit * mult
            sum += curr_digit ** 2

            mult*=10

        return sum

    def isHappy(self, n: int) -> bool:
        visited_set = set()
        while n not in visited_set:
            visited_set.add(n)
            n = self.sum_of_squares(n)
            
            if n == 1:
                return True

        return False