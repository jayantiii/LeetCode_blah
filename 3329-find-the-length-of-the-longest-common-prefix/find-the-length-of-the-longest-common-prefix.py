class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        m = len(arr2)
        hashmap = {} # process all possible prefixes of arr1
        maxcount = 0
        for i in range(len(arr1)):
            num = arr1[i]
            string = ""
            for n in str(num):
                string += n
                if string not in hashmap:
                    hashmap[string] = len(string)

        for i in range(len(arr2)):
            num = arr2[i]
            string = ""
            for n in str(num):
                string += n
                if string in hashmap:
                    maxcount = max(maxcount, hashmap[string])

        return maxcount



            




#number of pairs = n*m
        