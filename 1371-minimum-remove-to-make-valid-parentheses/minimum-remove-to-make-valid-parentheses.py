class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        liststring = list(s) # better to modify a list than string
        stack = [] #open parenthesis index

        for i,char in enumerate(liststring):
            if char == '(': #push to stack
                stack.append(i) #append index not char!!
            elif char == ')': #check if openparen in stack
                if not stack: #no open so remove it or empty string 
                    liststring[i] = ""
                else:
                    stack.pop() #found valid ) for (

            #if anything else just continue

        while stack: #if any ( left whose close ) we couldnt find
            i = stack.pop()
            liststring[i] = "" #make it empty string!!
        return "".join(liststring)
        
# 1)number of ( == number of )
#2) we ca never begin with ) and never end with open (
#3) Use stack to keep track of index of open ( and keep finding matching )
#Imp - Make the list such that for result u need to just join it

#Note - strings in Python are immutable.
# This means that once a string object is created, its content cannot be changed. Any operation that appears to modify a string, such as concatenation or using string methods like replace(), actually creates a new string object with the desired changes, and the variable is then reassigned to refer to this new object. 

#I thought this below thing, but if 1,2,3 valid then its valid, try examples!!
## even if number is equal, it can still be invalid based on order ->>not excatly