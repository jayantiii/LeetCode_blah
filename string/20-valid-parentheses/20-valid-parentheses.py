class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','[':']','{':'}'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] !=i: return False
        return len(stack) == 0
                
   

# My approach - failed cases passed few (eg: "([)]" output came true but expected false)

#         flag1 =0
#         flag2 = 0
#         flag3 = 0
#         for i in s:
#             if i =='(' : flag1 += 1
#             if i ==')' : flag1 -= 1
#             if i =='[' : flag2 += 1
#             if i ==']' : flag2 -= 1
#             if i =='{' : flag3 += 1
#             if i =='}' : flag3 -= 1
                
#         return flag1 == 0 and flag2 == 0 and flag3 ==0

            
                
            
        