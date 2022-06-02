class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','').replace('{}','').replace('[]','')
            if l==len(s): return False
        return True

    
    

    
    
    
    
    
#My approach - failed cases passed few (eg: "([)]" output came true but expected false)

        flag1 =0
        flag2 = 0
        flag3 = 0
        for i in s:
            if i =='(' : flag1 += 1
            if i ==')' : flag1 -= 1
            if i =='[' : flag2 += 1
            if i ==']' : flag2 -= 1
            if i =='{' : flag3 += 1
            if i =='}' : flag3 -= 1
                
        return flag1 == 0 and flag2 == 0 and flag3 ==0

            
                
            
        