class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # one deletion allowed: skip left OR skip right
                return is_pal(l + 1, r) or is_pal(l, r - 1)

        return True

#------------------Idea -------------
# If s[l] != s[r], you’re allowed to delete at most one character, so the only two valid options are:

# delete s[l] → check if s[l+1:r] is palindrome
# delete s[r] → check if s[l:r-1] is palindrome

#----------------My 2nd code works but TLE, O(n2) --------------------------
        # def is_pal(snew):
        #     l,r = 0, len(snew) -1
        #     while l<r:
        #         if snew[l] == snew[r]:
        #             l+=1
        #             r-=1
        #         else:
        #             return False
        #     return True

        # if is_pal(s): return True

        # for  i in range(len(s)):
        #     snew = s[:i] + s[i+1:]
        #     if is_pal(snew): return True

        # return False


#-----------MY First CODE BUGG, Wrong!!-----------------------------------
# The main bug is that you commit too early to deleting either the left or right side based on local comparison, instead of checking which deletion actually leads to a palindrome in the rest of the string. 
#because as soon as you choose one side, you lose the ability to “backtrack”.

#passed 470/477 but not right, interetsing bug!!
        # l,r = 0, len(s)-1
        # operation = False
        # while l<r:
        #     if s[l] ==s[r]:
        #         l+=1
        #         r-=1
        #     else:
        #         if operation:return False
        #         # Wrong thing to do
        #         if s[l+1] == s[r]: #delete left
        #             l = l+2
        #             r=r-1 #both l and r update

        #         elif s[l] == s[r-1]: #delete right
        #             r = r-2
        #             l=l+1
        #         else: return False
        #         operation = True
        # return True



            




