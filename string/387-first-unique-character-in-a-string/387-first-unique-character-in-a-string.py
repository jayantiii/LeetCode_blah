class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()           # look notes too
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                if s.count(s[i]) == 1:
                    return i
        return -1
       
# My second approach - very slow , can make it faster by above code
#  i = 0
#         for char in s:
#             if s.count(char) == 1:
#                 return i
#             i+=1
#             return -1
    
    
 # My first approach - passes all cases but can be made more efficient  
    # delstr =""
    #     for i in range(len(s)):
    #         char = s[0]
    #         s = s[1:]
    #         if char not in s and char not in delstr:
    #             return i
    #         delstr = delstr + char
    #     return -1