class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        strarr = list(s)
        sumarr = [0]*len(s)

        for i, shift in enumerate(shifts):
            start,end,direction = shift
            direction = -1 if direction == 0 else 1
            sumarr[start] += direction
            if end + 1 < len(s):
                sumarr[end+1] -= direction

        prefixsum = 0
        for i in range(len(s)):
            prefixsum += sumarr[i]
            shift = prefixsum % 26 ##IMP, how to take care of wrapping
            base = ord(strarr[i]) - ord('a')
            newchar = chr((base + shift)%26 + ord('a'))  #IMP
            strarr[i] = newchar

        return "".join(strarr)

#-----Interesting technique - Difference array and prefixsum------
#   Difference array idea:
#         - We want to add +delta or -delta to every index in [l, r].
#         - Instead of looping l..r (slow), we do:
#               diff[l]   += delta
#               diff[r+1] -= delta
#        Then the prefix sum of diff gives the net shift at each index.
#        Complete all queries using the method, then do prefixsum.

#         Why it works:
#         - Adding at l starts the effect from l onward.
#         - Subtracting at r+1 cancels the effect after r.
#         - Prefix sum accumulates all "active" range updates at each position.

#“mod 26” is literally the wrap-around rule (after z comes a, before a comes z).

#---------Brute force - TLE---------------------------------------     
        # arr = list(s)

        # for i, shift in enumerate(shifts):
        #     start,end,direction = shift
        #     direction = -1 if direction == 0 else 1
        #     j = start

        #     while j <= end:
        #         newcharascii = ord(arr[j]) + direction
        #         newchar =  chr(newcharascii)
        #         if arr[j] == "z" and direction == 1:
        #             newchar = "a"
        #         if arr[j] == "a" and direction == -1:
        #             newchar = "z"
        #         arr[j] = newchar
        #         j+=1

        # return "".join(arr)
       
#----Notes ------
#-- cant use split, use list()
# arr = s.split()  # # "abc" -> ["abc"]