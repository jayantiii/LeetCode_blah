class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        text = text.split(" ") #cant loop directly without this
        print(text)
        f, s = "", ""
        res = []
        for i in range(0,len(text)):
            
            third = text[i]
            if f == first and  s == second:
                res.append(third)
                
            f = s
            s= third
            
        return res
                
#Whenever see a string, think if u need to convert it ito a list
            
        