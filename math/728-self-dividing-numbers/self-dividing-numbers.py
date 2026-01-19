class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            for c in str(i): # string so make it iterable
                if  int(c)==0 or int(i) % int(c) != 0: #Needed - int(c)==0  
                    break

            else: #Interesting Syntax, -> else block outside loop!1
                res.append(i)

        return res
                    