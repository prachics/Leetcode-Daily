class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        
        has_vowel = False
        has_consonant = False
        
        for i in word:
            if i.isalpha():
                if i.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True
            elif not i.isdigit():
                return False
        
        return has_vowel and has_consonant

           

        