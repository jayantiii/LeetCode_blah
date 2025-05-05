class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i,j = 0,0
        count = 0 # we want it to be len of s
        while j < len(t) and i <len(s):
            if s[i] == t[j]:
                count +=1
                i+=1
                j+=1
            else:
                j+=1

        return count == len(s)


                
        

        