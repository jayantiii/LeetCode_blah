class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        # # dp[i] = number of ways to decode s[:i] #dp[2], 2 chars, but index 1 for string
        dp = [0]*(len(s)+1)
        dp[0] = 1 #empty string has one way
        dp[1] = 1
        for index in range(1,len(s)):
            i = index +1 #since we need to start fillin from dp[2] but take from s[1:]

            #If one digit
            if s[index] != '0':
                dp[i] = dp[i-1]

            #If can form 2 digit using previous
            if  10 <= int(s[index-1:index+1]) <= 26:
                dp[i] = dp[i] + dp[i-2]

        return dp[-1]

#dp[i] = number of ways to decode the first i characters (s[:i])   
#here i is the number of characters we’re taking from the start of the string, not a character index.
# dp[0] → ways to decode s[:0] → empty string ""
# dp[1] → ways to decode s[:1] → just s[0] (the 1st character)
# dp[2] → ways to decode s[:2] → s[0]s[1] (1st and 2nd characters)   

#Interesting line to use --> for i, ch in enumerate(s[1:], 2):
# Iterate over the characters of s starting from the second character (s[1]). 
# But label them with indices starting at 2, not 0.

# "   @lru_cache(maxsize=None)
#         def decode(i: int) -> int:
#             # i == len(s): we have successfully decoded the entire string
#             if i == len(s):
#                 return 1

#             # If current char is '0', this path is invalid
#             if s[i] == '0':
#                 return 0

#             # Option 1: take one digit (s[i] as a single letter)
#             ways = decode(i + 1)

#             # Option 2: take two digits (s[i:i+2] as a letter) if valid 10–26
#             if i + 1 < len(s):
#                 val = int(s[i:i+2])
#                 if 10 <= val <= 26:
#                     ways += decode(i + 2)

#             return ways

#         return decode(0)



# def decode(message):
        #     if not message: #if string empty, w ehave decoded everything
        #         return 1
        #     if message[0] == '0':#string #leading zero means just return
        #         return 0 #
            
        #     #option1 - decode using one digit
        #     onedigitpath = decode(message[1:])

        #     #option2 - decode using 2 digit,only if the 2 digit is valid
        #     twodigitpath = 0 # initialise or error cannot access local variable 
        #     if len(message) >=2:
        #         if int(message[:2]) >=10  and int(message[:2]) <=26:
        #             twodigitpath = decode(message[2:])

        #     return onedigitpath + twodigitpath            

        # return decode(s)
        