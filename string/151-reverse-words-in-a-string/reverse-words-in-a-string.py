class Solution:
    def reverseWords(self, s: str) -> str:
        sarr = s.split(" ")
        sarr = [x for x in sarr if x!= '']
        print(sarr)
        rev = sarr[::-1]
        print(" ".join(rev))
        return " ".join(rev).strip()



#  think about cases like s = "  hello world  "
