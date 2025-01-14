class Solution:
    def isValid(self, s: str) -> bool:
        #O(n),O(n)
        stack = []
        dic = { "}":"{", "]":"[", ")":"(" }
        for i in range(len(s)):
            if s[i] in dic: #took much time to think and form the if else block
                if stack and stack[-1] == dic[s[i]]:
                    stack.pop()
                else:
                    return False      
            else:
                stack.append(s[i])
        return stack == [] #or  return True if not stack else False

    
#brute force, O(n2),O(n)
# while '()' in s or '{}' in s or '[]' in s:
#             s = s.replace('()', '')
#             s = s.replace('{}', '')
#             s = s.replace('[]', '')
#         return s == ''