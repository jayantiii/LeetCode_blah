class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        #hint -- Count the frequency of each character in s and target. 
        freq = {}
        copies = 0
        for i in range(0, len(target)):
            freq[target[i]] = s.count(target[i])

        i = 0
        l = len(target)
        while True:
            print(freq)
            print(i,l-1)
            if freq[target[i]] > 0:
                freq[target[i]] -=1
            else:
                return copies
            if i ==l-1:
                copies +=1
                i=0
                continue
            i+=1


## passes 94/116 cases
        # freq = {}
        # copies = 0
        # for i in range(0, len(target)):
        #     freq[target[i]] = s.count(target[i])

        # i = 0
        # l = len(target)
        # while True:
        #     print(freq)
        #     print(i,l-1)
        #     if freq[target[i]] > 0:
        #         freq[target[i]] -=1
        #     else:
        #         return copies
        #     if i ==l-1:
        #         copies +=1
        #         freq[target[i]] -=1
        #         i=0
        #         continue
        #     i+=1


