class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1] #reverse
        b = b[::-1]
        carry = 0
        res = ""
        for i in range(max(len(a),len(b))):
            digita = int(a[i]) if i < len(a) else 0
            digitb = int(b[i]) if i <len(b) else 0

            total = digita + digitb + carry # add
            char = str(total % 2) # understand the logic
            res = char + res
            carry = total//2

        if carry:
            res = "1"+res

        return res



            
       



        





# If you are trying to convert the input strings into decimals, add them, and convert the number into a string, you're going to exceed a 64-bit integer. Therefore, think of a different approach.
# Concept of Binary Addition.
# **Rememeber,
# 1+1=0 with carry 1
# 1+0=1 with carry 0
# 0+1=1 with carry 0
# 0+0=0 with carry 0
# Imp:1+1=1 with carry 1 if previous carry was 1.
# The carry gets added in next step(scanning from right to left).
# **