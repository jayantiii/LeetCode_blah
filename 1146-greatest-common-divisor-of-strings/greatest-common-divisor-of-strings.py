class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        small = str2 if n > m else str1
        longg = str1 if n > m else str2
        s = n if n <m else m
        l = n if n > m else m
        prefix =  ""
        for i in range(s, 0, -1):
            c = len(small[0:i])
            print( small[0:i], i)
            if s%c == 0 and l % c == 0 :
                make = small[0:i] * (s//c)

                # print("make", make, s // len(small[0:i]))
                # print("long", (l // c) small[0:i] * (l//c), longg )
                if make == small and small[0:i] * (l//c) == longg:
                    prefix = small[0:i] 
                    
                    return prefix
            else: continue
        return prefix

# #The greatest common divisor must be a prefix of each string,try all prefixes
# # points to consider
# # - start with smaller string
# # - see if string divided length of it perfectly
# # - We can do reverse approach

# # min(m,n). (n + m)
#         x = str1 if len(str1) < len(str2) else str2
#         for i in range(len(x), -1, -1):
#             if len(x)%i != 0:
#                 continue
#             q1 = len(x)//i
#             if x[:i] * q1 == x:
#                 q2 
#                 if x[:i]*
#                 return x[:i]
#             else:
#                 return ""

# # wrong answer because wrong assumption  ( ABAB doesnt divide ABABAB) 
# # read carefully
#         # if len(str1) > len(str2):
#         #     if str2 in str1 and not "":
#         #         return str2
#         #     else:
#         #         for i in range(len(str2), -1, -1):
#         #             if str2[:i] in str1 and not "":
#         #                 return str2[:i]
#         #         return ""
                



        
