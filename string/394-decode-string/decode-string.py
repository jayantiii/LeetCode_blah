class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else: #means closing parenthesis
                curr =""
                while stack and stack[-1] != "[": #until not opening bracket
                    c = stack.pop()
                    curr = c + curr  #the order matters!!
                stack.pop() #remove the [              
                num = ""
                while stack and stack[-1].isdigit(): # it can be more than 1 digit so
                    n = stack.pop()
                    num = n+ num
                res = curr * int(num)
                stack.append(res)
                print(stack)
        return "".join(stack)



#its not that simple as it looks, brackets can be nested and there can be many chars within
#so whenever we notice pattern of working first the inner most [ ] then work way up - its stacks, "".join(stack)
        
#Loop through string and add to stack until u come across a closed bracket
#Also, understand the logic behind using stack for final answer

#s =
# "2[abc]3[cd]ef"
# Stdout, printing stack each for loop
# ['abcabc']
# ['abcabc', 'cdcdcd']


