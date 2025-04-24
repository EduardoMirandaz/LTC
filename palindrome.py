class Solution:
    def isPalindrome(self, s: str) -> bool:

        right_boundary = len(s) - 1 
        
        left_pointer, right_pointer = 0, right_boundary
        
        s = s.lower()
        
        while left_pointer < right_pointer:
            while(not s[right_pointer].isalnum() and right_pointer >= 0):
                right_pointer -= 1
            while(not s[left_pointer].isalnum() and left_pointer < right_boundary):
                left_pointer += 1

            if(s[left_pointer] != s[right_pointer]):
                return False

            left_pointer += 1
            right_pointer -= 1

        return True

