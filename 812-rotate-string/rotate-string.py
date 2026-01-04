class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False

        doubles = s + s #smart
        if goal in doubles:
            return True
        else: 
            return False
    

# Noticing patterns and forming insights: From the examples, we might notice that all the rotated strings are substrings of s + s = "abcdeabcde". Thus, we can check if goal is a substring of s + s to see if s can be rotated to form goal.

#----------------------------------Brute force, rotate and check-------------------------------
        # if len(s) != len(goal):
        #     return False
        # if s == goal:
        #     return True

        # n = len(s)
        # cur = s
        # for _ in range(n - 1):          # at most n-1 more distinct rotations
        #     cur = cur[1:] + cur[0]      # one left shift
        #     if cur == goal:
        #         return True
        # return False

