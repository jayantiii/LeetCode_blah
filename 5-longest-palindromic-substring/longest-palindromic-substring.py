class Solution:
    def longestPalindrome(self, s: str) -> str: 
        #let 0 is false, 1 is True, : O(n²) time, O(n²) space,
        dp = [[0]*len(s) for j in range(len(s))]
        best_l = best_r = 0  # inclusive indices of best palindrome

        for i in range(len(s)): #fill diagonal, Length 1
            dp[i][i] = 1

        #imp to think how to fill the grid, cant just normally row or col wise
        for length in range(2,len(s)+1):
            for i in range(0, len(s) - length + 1): #think how to calc range!
                start = i
                end = i+length -1 #Think
                if s[start] == s[end]:
                    #Check the middle
                    if  length <= 2 or dp[start+1][end-1] == 1:   # length <= 2 needed
                        dp[start][end] = 1
                        if length > best_r - best_l + 1: #+1 needed
                            best_r = end
                            best_l = start
                else:
                    dp[start][end] = 0 #not a a palindrome
        return s[best_l:best_r+1]


#2D DP
#IMP --- dp[i][j] depends on a smaller substring inside it: dp[i+1][j-1]. [THINK HOW]
#Diagonal elements is single element palindrome true
#    0 1 2 3 4
#    b a b a d
# b. 1    
# a    1      0 (1,4)
# b      1   
# a         1
# b           1



#---------------------------idea but not work ------------
#  we can reverse the string and try to find longest common substring between s and s'
#But this dont work # Longest Palindromic Subsequence (LPS) For subsequence, order matters but contiguity doesn’t.

#----------- Another Apporach to solve ---------------------
#  solved it using Rolling Hash matrices!
# You make two n by n matrices, one for the string and one for the reversed string. Build a randomized rolling hash procedure that is sufficiently fast to fill two suffix hash matrices with 64-bit integers.
# Comparing each index of the first matrix with the second takes O(1) time and yields collision if a palindrome is found (with high probability). Overall time complexity is then O(n^2) for building your two n by n matrices, and then for comparing each of their indices.

#-----------Bruteforce - #find all substrings and check if they palindrome, 0(n.n2) so O(n3) ----
        # def ispal(subs):
        #     l,r = 0, len(subs)-1
        #     while l <= r:
        #         if subs[l] == subs[r]:
        #             l+=1
        #             r-=1
        #         else:
        #             return False
        #     return True 

        # longest = ""
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substring = s[i:j+1]
        #         if ispal(substring):
        #             longest = substring if len(substring) > len(longest) else longest
        # return longest

##---- Top down, O(n²) distinct (i, j) states for is_pal(i, j). ------------------
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n <= 1:
    #         return s

    #     best_l = best_r = 0  # inclusive

    #     @lru_cache(maxsize=None)
    #     def is_pal(i: int, j: int) -> bool:
    #         if i >= j:            # length 0/1
    #             return True
    #         if s[i] != s[j]:
    #             return False
    #         return is_pal(i + 1, j - 1)

    #     # try all substrings, memo makes palindrome-check O(1) amortized per state
    #     for i in range(n):
    #         for j in range(i, n):
    #             if (j - i) > (best_r - best_l) and is_pal(i, j):
    #                 best_l, best_r = i, j

    #     return s[best_l:best_r + 1]
        