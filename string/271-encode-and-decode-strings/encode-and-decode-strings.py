class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = ""
        for word in strs:
            enc = enc + str(len(word)) + "#" + word
        print(enc)
        return enc                  

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            # read full number (can be multi-digit)
            j = i
            while s[j] != "#": #while needed
                j+=1
            num = int(s[i:j]) #not j+1

            word = s[j+1:j+1 +num] # understand the j+1 +num
            res.append(word)
            i = j+ num + 1

        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

#Idea
# "Hello","World" -- > "5#Hello5#World" 
#we do like this because if we only use # this to seperate what if a word has # this in it

#Mymistake!!!, handles only 1-digit lengths also dont do s[i].isdigit() cause what if a word has a digit!!
#  if s[i].isdigit() and s[i+1] == "#": - wrong
#This only works if the length is like 3#.... If the length is 12#..., then s[i+1] is '2', not '#', so the condition fails and you never decode anything.