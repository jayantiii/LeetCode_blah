class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = bin(n)[2:]
        res = 0
        print(bit)
        # O(1) because max is O(32) that is constant
        for b in bit:
            if int(b) == 1:
                res+=1
        return res

#another idea
# while bit:
#         res += bit % 2.  -- 2 modulo with 1 is 1, with zero is zero
#         n = n >>1     -- shift right by one bit
#      return res
    
# a way to convert dec to bits
# DecimalToBinary(num):
#         if num >= 1:
#             DecimalToBinary(num // 2)
#            print num % 2 

#another way - bin(n).replace("0b", "") or bin(4785)[2:]

#one line - return bin(n).count('1')