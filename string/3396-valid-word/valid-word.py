class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        vowels = "aeiouAEIOU"
        vowel, cons = False, False
        for char in word:
            if 48 <= ord(char) <= 57:
                pass
            elif 65 <= ord(char) <=90 or 97 <= ord(char) <=122:
                if char in vowels:
                    vowel = True
                else:
                    cons = True
            else:
                return False
        
        return vowel and cons

#ASCII
# 48-57 is 0 to 9
# 65-90 is A-Z
# 97-122 isa-z

#Better way and simpler, use isalpha, isdigit and vowelset
    #    if len(s) < 3:
    #         return False

    #     vowels = 0
    #     consonants = 0
    #     vowel_set = "aeiouAEIOU" #consider both

    #     for c in s:
    #         if c.isalpha():
    #             if c in vowel_set:
    #                 vowels += 1
    #             else:
    #                 consonants += 1
    #         elif not c.isdigit():
    #             return False  # invalid character

    #     return vowels >= 1 and consonants >= 1

    
        