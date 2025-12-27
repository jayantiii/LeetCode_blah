class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        currcount,prevchar = 1, s[0]
        totalcount = 0
        for char in s[1:]:
            if char == prevchar:
                currcount +=1
            else:
                totalcount+= int(currcount*(currcount +1)//2)
                prevchar = char #reset
                currcount = 1 #reset

         # flush last run - IMPP I always forget
        totalcount += currcount * (currcount + 1) // 2
        return totalcount % MOD

##IMP --- formula is n(n+1)/2
#Hint
# A string of only 'a's of length k contains k + 1 choose 2 homogenous substrings.
#----------How to come up with the formula ---------
# If a run has length 4 (say "aaaa"), count homogenous substrings inside it:

# By lengths:

# length 1: a a a a → 4

# length 2: aa aa aa → 3

# length 3: aaa aaa → 2

# length 4: aaaa → 1

# Total = 4 + 3 + 2 + 1 = 10





        