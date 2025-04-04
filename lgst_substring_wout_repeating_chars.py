class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        length_biggest_substring = 0

        count = 0
        substr_hashmap = {}
        for i, l in enumerate(s):

            if l in substring:
                length_biggest_substring = max(count, length_biggest_substring)
                # substring = substring[substring.find(l)+1:]+l
                substring = substring[substr_hashmap[l]+1:] + l
                substr_hashmap[l] = len(substring) - 1
                count = len(substring)
            else:
                count+=1
                substring+=l
                if(l not in substr_hashmap):
                    substr_hashmap[l] = len(substring)-1


        return max(count, length_biggest_substring)