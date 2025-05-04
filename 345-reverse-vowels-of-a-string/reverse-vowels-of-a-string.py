class Solution:
    def reverseVowels(self, s: str) -> str:
        #use 2 pointers


        s = list(s)  # string are not mutable in python !!! convert to list
        l,r = 0 , len(s) -1 # use while for l and r
        vowel = set("aeiouAEIOU") #  wrong -- vowel = ['a','e','i','o','u'] 
        
        while l <=r:
            if s[l] in vowel and s[r] in vowel:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l+=1
                r-=1
            else:
                if s[l] in vowel:
                    r = r-1
                else:
                    l=l+1
        return  "".join(s)          #s.join() -wrong

