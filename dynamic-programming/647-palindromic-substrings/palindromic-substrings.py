class Solution:
    def countSubstrings(self, s: str) -> int:
        #dp[i][j] = #true if  i...j is a palindrome substrings
        n = len(s)
        dp = [[False]* (n) for i in range(n)] #no need of n+1 here
        ans = 0

        #diagonals, we dont need it as next loop handles it too
        for i in range(n): 
            dp[i][i] = True

        # The recurrence needs dp[i+1][j-1] already computed so think how fill!
        for i in range(n-1,-1,-1):
            for j in range(i,n): #since left half not valid
                if s[j] == s[i]:
                    # j - i <= 1 is a shortcut for “the substring length is 1 or 2”.

                    if (j-i)<=1 or dp[i+1][j-1]: 
                        dp[i][j] = True
                        ans+=1

        return ans
                

#IMP --- dp[i][j] depends on a smaller substring inside it: dp[i+1][j-1].
#       r →
#         0 1 2 3 4
# l 0     ✓ ✓ ✓ ✓ ✓
# ↓ 1       ✓ ✓ ✓ ✓
#   2         ✓ ✓ ✓
#   3           ✓ ✓
#   4             ✓

# (lower triangle l>r is unused)

# if (j-i)<=1 or dp[i+1][j-1]: 
#the order matters (j-i)<=1 before , acts as boundary check for i+1, j-1

#-------------- Why (j - i <= 1)?-----------------------
# dp[i][j] wants to look "inside" at dp[i+1][j-1].
# But for very short substrings, there is no real "inside":
#   - length 1 (j==i): inside is dp[i+1][i-1]  -> invalid/empty
#   - length 2 (j==i+1): inside is dp[i+1][i]  -> empty
# So for length 1 or 2, if the end chars match, it's automatically a palindrome.
# That's exactly what (j - i <= 1) checks: length = (j - i + 1) is 1 or 2.

#----------------------Why we dont need dp size n+1 * n+1 but n*n-----------------
# # “Substrings” here means non-empty contiguous pieces of s.
# So you do not count the empty string.
# In the DP code, that’s why we start with length = 1 (not 0).

#----------------------------Exapnd around center method--------------------
#    def countSubstrings(self, s: str) -> int:
#         n = len(s)

#         def expand(l: int, r: int) -> int:
#             cnt = 0
#             while l >= 0 and r < n and s[l] == s[r]:
#                 cnt += 1
#                 l -= 1
#                 r += 1
#             return cnt

#         ans = 0
#         for c in range(n):
#             ans += expand(c, c)       # odd length
#             ans += expand(c, c + 1)   # even length
#         return ans
