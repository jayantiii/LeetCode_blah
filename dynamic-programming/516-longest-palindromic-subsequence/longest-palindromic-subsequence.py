class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for i in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-2,-1,-1): #fill from last second row
            for j in range(i+1,n): #only rows (i+1,n can be filled)

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2 # add plus 2, not just 1!!
                else:
                    #IMP-->, drop either left or right!! #->dp = 1 is wrong
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1]) 

        return dp[0][-1]

#Here --> dp[i][j] depends on [i+1][j-1]

# dp[i][j] = the length of the longest palindromic subsequence inside the substring s[i..j] (inclusive).
# dp[i][j] is the maximum length of any palindromic subsequence you can pick using only characters from indices i..j.

#ELSE condition!!!
# It means: if the two ends don’t match, they can’t both be in the same palindromic subsequence, so at least one of them must be excluded.

##---------------------------ANOTHER WAY----------------------------
# you can compute LPS by doing LCS(s, reverse(s)), because any palindromic subsequence reads the same forward and backward, so it appears in both strings.

##Why cant we do similar way for LP substring?
# “what if we do longest common substring of s and reverse(s)?” — still not reliable for longest palindromic substring.
# Why: a common substring just means “this block appears in both strings.” In reverse(s), that block corresponds to the reverse of some other location in s, so you can match a substring with the reverse of a different substring — not necessarily a palindrome at the same mirrored indices.

#---------Subsequence and substring difference code-----------------------------
# SUBSEQUENCE (can skip chars)
# dp[i][j] = best (max length) palindrome you can build using chars only from s[i..j]
# if ends match -> take both ends + best inside
# if ends differ -> you must drop one end (skip i OR skip j), take the better
# dp[i][j] = max(dp[i+1][j], dp[i][j-1])

# SUBSTRING (must be continuous)
# You can't "drop an end" and keep contiguity in a simple max DP.
# Instead, check if the whole interval s[i..j] itself is a palindrome.
# isPal[i][j] = True if s[i..j] is palindrome substring
# isPal[i][j] = (s[i]==s[j]) AND (length<=3 OR isPal[i+1][j-1])
# While filling, remember the longest (i,j) where isPal[i][j] == True

        