class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = rowIndex
        res = [1]
        for i in range(r):
            temp = [0] + res + [0]
            print(temp)
            row = []
            for j in range(len(temp)-1):
                row.append(temp[j] + temp[j+1])
            res = row
            print(res)
        return res
            
        