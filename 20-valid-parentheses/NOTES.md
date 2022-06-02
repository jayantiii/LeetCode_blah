**###takes more time**
while len(s) > 0:
l = len(s)
s = s.replace('()','').replace('{}','').replace('[]','')
if l==len(s): return False
return True
#If we have a string of the type: s="( [ ] ) { } ", I suspect this logic won't work.
So the assumption of the question and solution must be that a parenthesis opened will be followed immediately by it's counterpart to close without any intervening parenthesis of another type.
​
#This logic will work with the string "( [ ] ) { } ".
After the first iteration, we will find '[]' and '{}' and remove we will them. So that we will get the string "()". Since the length of the string has changed we assume that we have found at least one of the three patterns and removed them. If so we have to check the new string that we have received after the removal.
The second iteration will find '()' in the string and will remove that. So that string will become empty.
If the string is empty then the initial string is valid and we will return True.