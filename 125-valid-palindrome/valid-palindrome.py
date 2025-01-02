import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        ss = re.sub(r'[^a-zA-Z0-9]','',s)
        return ss == ss[::-1]

# 2 pointer way, to be efficient, use two pointer algo
    # i, j = 0, len(s) - 1
    #     while i < j:
    #         while i < j and not s[i].isalnum(): i += 1
    #         while i < j and not s[j].isalnum(): j -= 1
    #         if s[i].lower() != s[j].lower(): return False
    #         i += 1
    #         j -= 1
    #     return True

#bitwise not operator
    #  s = [c.lower() for c in s if c.isalnum()]
    #     return all (s[i] == s[~i] for i in range(len(s)//2))

#filtered = ''.join(c for c in s if c.isalnum()) - one other way

#write own isalphanum function
#   def alphaNum(self, c):
#         return (ord('A') <= ord(c) <= ord('Z') or 
#                 ord('a') <= ord(c) <= ord('z') or 
#                 ord('0') <= ord(c) <= ord('9'))