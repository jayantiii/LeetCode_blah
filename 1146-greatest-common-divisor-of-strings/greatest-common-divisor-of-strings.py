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
                



        