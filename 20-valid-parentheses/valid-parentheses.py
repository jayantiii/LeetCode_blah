class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #({[]})
        dic = { "}":"{", "]":"[", ")":"(" }
        for i in range(len(s)):
            if s[i] in dic:
                if stack != [] and stack[-1] == dic[s[i]]:
                    stack.pop(-1)
                    continue
                else:
                    return False      
            else:
                stack.append(s[i])
        return stack == []

    
#brute force, O(n2),O(n)
# while '()' in s or '{}' in s or '[]' in s:
#             s = s.replace('()', '')
#             s = s.replace('{}', '')
#             s = s.replace('[]', '')
#         return s == ''