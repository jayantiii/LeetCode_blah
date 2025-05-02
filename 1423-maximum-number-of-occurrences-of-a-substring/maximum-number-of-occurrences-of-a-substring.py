class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
         # o(n), o (n)
        #1 <= maxLetters <= 26 means explore all substrings in O(n * 26).
        maxocc = 0
        freq = {}
        for i in range(0, len(s) - minSize +1 ):
            sub= s[i:i+ minSize] # no plus 1
            if len(set(sub)) <= maxLetters:
                f = freq.get(sub,0)
                freq[sub] = f + 1
                maxocc = max(maxocc, freq[sub])
        return maxocc
            



        

#Hint :- Just ignore maxSize because char present in long string(repeasted) also present in same small string
#recognize that if we have a minSize 3 and maxSize 5
# We can identify that substring 3 will be in substring 4 and substring 5
# Which means we only have to check the min size
