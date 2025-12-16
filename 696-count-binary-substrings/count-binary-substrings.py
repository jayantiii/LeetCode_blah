class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_len, current_len = 0,1
        count = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                current_len+=1
            else:
                prev_len = current_len
                current_len =1 

            ## If the previous length is greater than or equal to the current length
            # then we have a valid substring
            if prev_len >= current_len: #this is the main logic
                count +=1

        return count

# Similar but little different way

#Note, zeros and 1s should be grouped together
#So,
#1) in a valid grouped substring, we get min(zerocount,onecount) substrings
#2) so find total  valid grouped substrings present
#3) and add the min(zerocount,onecount) for all

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         prev_run = 0
#         cur_run = 1
#         ans = 0

#         for i in range(1, len(s)):
#             if s[i] == s[i - 1]:
#                 cur_run += 1
#             else:
#                 ans += min(prev_run, cur_run).    #this is the imp part
#                 prev_run, cur_run = cur_run, 1

#         ans += min(prev_run, cur_run) # #this is the imp part too
#         return ans


# Eg: "00011100" --> [3 zeroes, 3 ones, 2 zeroes] --> [3,3,2] --> Ans = min(3,3) + min(3,2) = 5 Total Substrings