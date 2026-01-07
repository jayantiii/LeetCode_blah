class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        v = []
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                k = list(s)
                k[i] = '-'
                k[i + 1] = '-'
                v.append("".join(k))
        return v


        