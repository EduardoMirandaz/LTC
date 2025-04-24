class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        len_s, len_t = len(s), len(t)
        if(len_s != len_t):
            return False


         # Considering that we will have only 26 letters
        letters_count = [0] * 26

        for idx in range(len_s):
            letters_count[ord(s[idx]) % 26] += 1
            letters_count[ord(t[idx]) % 26] -= 1

        return letters_count == [0] * 26


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_letters_count = {}
        t_letters_count = {}

        for char in s:
            s_letters_count = s_letters_count.get(char, 0) + 1

        for char in t:
            t_letters_count = t_letters_count.get(char, 0) + 1


        return s_letters_count == t_letters_count


