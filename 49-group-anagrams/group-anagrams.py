class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # tc = (m*nlogn) where n is length of longest string
        #sc = O(m*n)
        res = defaultdict(list)
        for s in strs:
            sortedw = ''.join(sorted(s)) #sorted makes it array like [a,e,t]
            print(sortedw)
            res[sortedw].append(s)

        return list(res.values())

#hash - O(mxn) , O(m), m is no. of strings
        # res = defaultdict(list)
        # for word in strs:
        #     count = [0] *  26
        #     for l in word:
        #         count[ord(l) - ord('a')] +=1
        #     res[tuple(count)].append(word)
        # print(res)
        # return list(res.values())


        
            
        