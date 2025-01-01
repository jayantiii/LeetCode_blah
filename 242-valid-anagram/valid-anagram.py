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
        
#anagram is not equal to palindrome (dont confuse)
# return sorted(s) == sorted(t)   - O(nlogn+mlogm) 
# return counter(s) == counter(t) - similar efficency as submitted soln

#more optimal way
#  count = [0] * 26
#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1

#         for val in count:
#             if val != 0:
#                 return False
#         return True

        
        