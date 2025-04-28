class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = 0
        single_letter = 0
        seen = []
        for l in s:
            if l in seen: continue
            seen.append(l)
            amount_of_l = s.count(l)
            
            if(amount_of_l % 2 == 0):
                c+=amount_of_l
            else:
                c+=amount_of_l-1
                single_letter = 1
        return c + single_letter