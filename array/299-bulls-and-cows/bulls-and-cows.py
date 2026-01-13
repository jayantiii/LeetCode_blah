class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = Counter(secret)

        bulls, cows =0,0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls +=1
                s[guess[i]] -=1
            
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                continue
            if guess[i] in s and s[guess[i]] >0:
                cows+=1
                s[guess[i]] -=1
        return str(bulls) + "A" + str(cows) + "B"

#My major mistake - I tried counting bulls and cows in one pass(oneloop)------>
# The problem: a digit in guess can match a digit in secret either as a cow or as a bull, but bulls must take priority. With your one-pass cow counting, you can “spend” a digit as a cow, and then later you reach the position where that digit should have been a bull — and you still count the bull too. That overcounts cows.
# core flaw: counting cows using only secret’s counts in a single left-to-right pass doesn’t enforce bull priority across future positions.

##------------------------- Other soln, no hashing, one pass-------------------------------
# Traverse both strings simultaneously.
# If characters match exactly, count it as a bull.
# If not, count their occurrences in separate frequency arrays.
# After traversal, count cows as the minimum of corresponding digit counts.


#         bulls = cows = 0
#         freq_secret = [0] * 10
#         freq_guess = [0] * 10

#         for s, g in zip(secret, guess):
#             if s == g:
#                 bulls += 1
#             else:
#                 freq_secret[int(s)] += 1
#                 freq_guess[int(g)] += 1

#         for i in range(10):
#             cows += min(freq_secret[i], freq_guess[i])

#         return f"{bulls}A{cows}B"



        