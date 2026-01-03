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

# The problem: a digit in guess can match a digit in secret either as a cow or as a bull, but bulls must take priority. With your one-pass cow counting, you can “spend” a digit as a cow, and then later you reach the position where that digit should have been a bull — and you still count the bull too. That overcounts cows.
# core flaw: counting cows using only secret’s counts in a single left-to-right pass doesn’t enforce bull priority across future positions.



        