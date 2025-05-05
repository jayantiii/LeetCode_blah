class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i,j = 0,0
        count = 0 # we want it to be len of s
        while j < len(t) and i <len(s): #  and i <len(s) important or will fail some cases
            if s[i] == t[j]:
                count +=1
                i+=1
                j+=1
            else:
                j+=1

        return count == len(s)

# similar!
#      sp = tp = 0

        # while sp < len(s) and tp < len(t):
        #     if s[sp] == t[tp]:
        #         sp += 1
        #     tp += 1
        
        # return sp == len(s)
                
        

        