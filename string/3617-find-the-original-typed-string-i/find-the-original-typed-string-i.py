class Solution:
    def possibleStringCount(self, word: str) -> int:
        prevchar = word[0]
        ways = 1 # for original
        for i in range(1,len(word)):
            if word[i] == prevchar:
                ways+=1
            prevchar = word[i]

        return ways


#keyword -  done this at most once and number of possible original strings 
#-------My first ans, wrong, i didnt get the question------------------
#       return len(set(word)) - This is wrong 
#exampke - "abbcccc", output gives 3 but answer is 5

#---------------------Why no DP / backtracking--------------------
# DP/backtracking is for when choices interact across positions (one choice changes what’s possible later). Here, “at most once” makes the structure additive: you either choose which run was affected (independent) and how much to shrink it. That collapses into a simple sum.