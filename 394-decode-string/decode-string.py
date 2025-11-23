class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else: #means closing parenthesis
                curr =""
                while stack and stack[-1] != "[":
                    c = stack.pop()
                    curr = c + curr 
                stack.pop() #remove the [              
                num = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop()
                    num = n+ num
                res = curr * int(num)
                stack.append(res)
                print(stack)
        return "".join(stack)



#its not that simple as it looks, brackets can be nested and there can be many chars within
#so whenever we notice pattern of working first the inner most [ ] then work way up - its stacks
        
#Loop through string and add to stack until u come across a closed bracket
#Also, understand the logic behind using stack for final answer


