class Solution:
    def maxPower(self, s: str) -> int:
        power = 1 #start with 1 ( min possible)
        prevchar = s[0]
        currpower = 1
        for i in range(1,len(s)):
            if s[i] == prevchar:
                currpower +=1
                power = max(currpower, power)
            else:
                currpower = 1 #dont forget to restart
            prevchar = s[i]
        return power


        