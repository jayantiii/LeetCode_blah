class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = bin(n)[2:]
        res = 0
        print(bit)
        for b in bit:
            if int(b) == 1:
                res+=1
        return res

        


# a way to convert dec to bits
# DecimalToBinary(num):
#         if num >= 1:
#             DecimalToBinary(num // 2)
#            print num % 2 
#another way - bin(n).replace("0b", "") or bin(4785)[2:]