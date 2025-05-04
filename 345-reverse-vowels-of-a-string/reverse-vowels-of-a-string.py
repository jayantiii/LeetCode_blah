class Solution:
    def reverseVowels(self, s: str) -> str:
        #use 2 pointers


        s = list(s)  # IMP - string are not mutable in python !!! convert to list
        l,r = 0 , len(s) -1 # use while for l and r
        vowel = set("aeiouAEIOU") #  wrong -- vowel = ['a','e','i','o','u'] 
        
        while l <=r:
            if s[l] in vowel and s[r] in vowel: # dont confuse when writing conditions
                temp = s[l]
                s[l] = s[r]
                s[r] = temp   # or can do s[i], s[j] = s[j], s[i]
                l+=1
                r-=1
            else:
                if s[l] in vowel:
                    r = r-1
                else:
                    l=l+1
        return  "".join(s)          #s.join() -wrong

##smaller
#   vowels=[i for i in s if i in "aeiouAEIOU"] 
#- Extract all vowels from the string into a list in order
# rebuild string
#    result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
#   return "".join(result)