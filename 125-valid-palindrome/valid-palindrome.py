import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #to be efficient, use two pointer algo
        s = s.lower().strip()
        ss = re.sub(r'[^a-zA-Z0-9]','',s)
        print(ss)

        return ss == ss[::-1]

#filtered = ''.join(c for c in s if c.isalnum())