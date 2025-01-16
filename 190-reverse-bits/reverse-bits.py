class Solution:
    def reverseBits(self, n: int) -> int:
        #bin(n)[2:] removes the 0b prefix but only includes the significant digits of the binary number.
        s = str(bin(n)[2:]).zfill(32)
        print(s, s[::-1])
        return int(s[::-1],2)
        