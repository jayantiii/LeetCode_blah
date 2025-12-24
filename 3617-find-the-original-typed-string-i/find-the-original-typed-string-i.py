class Solution:
    def possibleStringCount(self, word: str) -> int:
        prevchar = word[0]
        ways = 0
        for i in range(1,len(word)):
            if word[i] == prevchar:
                ways+=1
            prevchar = word[i]

        return ways + 1







#keyword -  done this at most once and number of possible original strings 

#My first ans, wrong, i didnt get the question
#       return len(set(word)) - This is wrong 
#exampke - "abbcccc", output gives 3 but answer is 5