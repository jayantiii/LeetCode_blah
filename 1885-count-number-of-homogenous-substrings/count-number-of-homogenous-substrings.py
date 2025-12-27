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

##IMP --- formula is n(n+1)/2.
#----------How to come up with the formula -----------------
# If a run has length 4 (say "aaaa"), count homogenous substrings inside it:
# By lengths:
# length 1: a a a a → 4
# length 2: aa aa aa → 3
# length 3: aaa aaa → 2
# length 4: aaaa → 1
# Total = 4 + 3 + 2 + 1 = 10


#---------- Another way ( almost same math) ---------------------
# You use run like this:
# run tells you how many same-char substrings end at the current index.
# So every time you update run, you add it to the total.
# That’s the whole method.
# Example: s = "aaab"
# Step by step (total starts 0):
# index 0 'a': run = 1 → total += 1 → total = 1
# index 1 'a': run = 2 → total += 2 → total = 3
# index 2 'a': run = 3 → total += 3 → total = 6
# index 3 'b': run = 1 → total += 1 → total = 7

# MOD = 10**9 + 7
# total = 0
# run = 0
# prev = ""

# for ch in s:
#     if ch == prev:
#         run += 1
#     else:
#         prev = ch
#         run = 1
#     total = (total + run) % MOD





        