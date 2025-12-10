class Solution:
    def kthCharacter(self, k: int) -> str:
        word ="a" 

        def game(word):
            #Base case
            if len(word) >= k:
                return word

            newword = ""
            for c in word:
                ch = ord(c) + 1 #ascii number
                newchar = chr(ch) #number to char
                if c == 'z': #for z
                    newchar='a'
                newword = newword + newchar

            return game(word + newword) # do return game() to make it recursive
        
        finalword = game(word)
        return finalword[k-1]
        
#every turn- create new string
        #    - change each char to its next
        #    - append to newstring to original string
#RECURSION!!! I DIDNTTHINK ABOUT THIS, COOL!!
        