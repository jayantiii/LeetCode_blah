class Solution:
    def getSum(self, a: int, b: int) -> int:
    # can be negative too
        return int(math.log(2 ** a * 2 ** b, 2))
    

# Mathematically, we rely on the identity:
#     2^a * 2^b = 2^(a+b)
# Taking log base 2 on both sides:
#     log2(2^a * 2^b) = a + b
#
# Therefore, in theory:
#     a + b == log2(2^a * 2^b)


# Wronggg Try!!
#         carry = 0
#         i = max(len(a),len(b))
#         sum = ''
#         while i>= 0:
#             sum = a[i] + b[i] + carry
#             carry += (sum // 10)
#             digit = sum % 10 
#             sum = digit+ sum
#             i-=1

#         return int(sum)
        