class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #look notes - for good for interview ans
        if len(s) != len(t):
            return False
        
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
            
        return True
    
# One line solutions
    
# return ''.join(sorted(t)) == ''.join(sorted(s))  # -- O(nlogn) 
    
# return Counter(s) == Counter(t)   #-- O(n)        
           
# return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
    
# The all() function returns True if all items in an iterable are true, otherwise it returns False.If the iterable object is empty, the all() function also returns True.