class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine_letters_count = {}

        for letter in magazine:
            if(letter in magazine_letters_count):
                magazine_letters_count[letter] += 1
            else:
                magazine_letters_count[letter] = 1
        
        for letter in ransomNote:
            if letter not in magazine_letters_count or magazine_letters_count[letter] <= 0:
                return False
            else:
                magazine_letters_count[letter] -= 1
        
        return True