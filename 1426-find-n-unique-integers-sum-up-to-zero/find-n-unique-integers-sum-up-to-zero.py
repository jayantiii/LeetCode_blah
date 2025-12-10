class Solution:
    def sumZero(self, n: int) -> List[int]:
        integer = 1
        res = []
        while n-2>=0:
            res.append(integer)
            res.append(integer* -1)
            integer +=1
            n=n-2
        if n ==1:
            res.append(0)
        #add if n =1, add -0 or leave
        return res
        


#if even, return +x,-x symmteric values
#if if odd, jus append 0 to it