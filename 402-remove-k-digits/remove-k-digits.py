class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
#Maintin digits in ascending order
#we want to remove digits in such a way, that we convert the digits in ascending order as close as possible
        #start from left hand side
        stack = []
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0: #there s dip so, and dont use if
                highele = stack.pop()
                k -=1
            stack.append(num[i]) #append current digit
        
        # After the loop, if k is still > 0, remove from the end.
        while k > 0 and stack: 
            stack.pop()
            k-=1
        res = "".join(stack).lstrip("0") # remove leading zeros
        return res if res else "0"

        
#Example
# num = 372181, k = 1
# - in this case even though 8 is the biggest, ans is 7 , that removing 7 will give smallest!!
# - understand the initution, try to flatten the curve from left side
# - whenever there is a dip, process it, try maintain stack in ascending order
# - techdose has good video on it

##---- My mistakes -------------------------------------
# After the loop, if k is still > 0, remove from the end. 
# Because after the main loop, your stack is non-decreasing (digits are in ascending order). In a non-decreasing sequence, the rightmost digits are the largest and also the least significant, so removing from the end gives the smallest possible remaining number.

#if k == 0: break is wrong → you must still append the remaining digits (breaking drops them).

#------------------How to know it’s a stack problem (intuition)-----
# This is a “make the number smallest after deleting k digits” problem. Two clues scream monotonic stack:

# Local choice affects global lexicographic order
# The leftmost digits matter most. If you can make an earlier digit smaller, that dominates any improvements later.

# “Whenever there’s a dip, delete the previous peak”
# If you have ... 7 3 ... and you’re allowed to delete something, deleting the 7 is always better than deleting the 3 because it makes the number smaller earlier. That’s exactly “pop while previous digit > current digit”.

# A stack is the natural structure because:
# You build the answer left to right.
# When a new digit arrives, you might need to “undo” previous choices (pop).
# That undo pattern is LIFO → stack.

# ##==========Interview explanation -------------

# We want the smallest number after removing k digits. The most significant digits matter most, so whenever we see a digit that is smaller than the previous digit, it’s beneficial to remove the previous larger digit if we still have removals left.
# This suggests a monotonic increasing stack: keep digits increasing; when a smaller digit comes, pop larger digits while k>0. After processing all digits, if k remains, remove from the end (largest tail). Finally strip leading zeros.
