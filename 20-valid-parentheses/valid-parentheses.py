class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { "(":")", "[":"]", "{":"}"}
        for x in s:
            if x in hashmap: #open bracket
                stack.append(x)
            else:
                if not stack: return False
                open = stack.pop()
                if hashmap[open] != x:
                    return False

        return True if not stack else False

    