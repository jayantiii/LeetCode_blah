class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = {}
        tcount = {}
        for i in range(len(s)):
            scount[s[i]] = 1 + scount.get(s[i],0) 
            tcount[t[i]] = 1 + tcount.get(t[i],0) 
        return scount == tcount

# return sorted(s) == sorted(t)   - O(nlogn+mlogm)  


#anagram is not equal to palindrome (dont confuse)
        
        