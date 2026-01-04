class Solution:
    def makeFancyString(self, s: str) -> str:
        resstr = s[:2]
        for i in range(2,len(s)):
            if s[i] == s[i-1] == s[i-2]:
                continue
            resstr = resstr +s[i]
        return resstr


# Tip - > do not delete anything from the string cuz it will lead to TLE, build another string instead