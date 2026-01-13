class Solution:
    def makeFancyString(self, s: str) -> str:
        resstr = s[:2]
        for i in range(2,len(s)):
            if s[i] == s[i-1] == s[i-2]:
                continue
            resstr = resstr +s[i]
        return resstr


# Tip - > do not delete anything from the string cuz it will lead to TLE, build another string instead
#------------------one more way, use list----------------------------------
    #    res = []
    #     for c in s:
    #         if len(res) >= 2 and res[-1] == c and res[-2] == c: ##check from result string!
    #             continue
    #         res.append(c)
    #     return ''.join(res)

##-----------------------Why “don’t delete from the string”:---------------------
# Python strings are immutable. Every “delete” or concatenation like ans += c creates a new string 
# → repeated copies → can degrade to O(n²) time.
#List append is amortized O(1), and ''.join(res) is O(n) total.