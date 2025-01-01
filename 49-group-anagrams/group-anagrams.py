class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            sortedw = ''.join(sorted(s)) #sorted makes it array like [a,e,t]
            print(sortedw)
            res[sortedw].append(s)

        return list(res.values())
        # res = defaultdict(list)
        # for word in strs:
        #     count = [0] *  26
        #     for l in word:
        #         count[ord(l) - ord('a')] +=1
        #     res[tuple(count)].append(word)
        # print(res)
        # return list(res.values())


        
            
        