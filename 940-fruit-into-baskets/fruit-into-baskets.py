class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #Idea - Find longest continous subarray that has atmost 2 distinct fruits!!
        n = len(fruits)
        maxlen= 0
        s,e = 0 ,0
        hashmap = {} #have only 2 at a point, store the value and last index it was seen on
        #Main is to figure out how to move the pointers
        while e < n:
            hashmap[fruits[e]] = e
            if len(hashmap) > 2: #then remove the smallest index
                minindex = min(hashmap.values())
                delval = fruits[minindex]
                del hashmap[delval]
                s =minindex + 1 #Understand
            maxlen = max(maxlen, e -s +1)
            e+=1
        return maxlen






       





#Brute force that works but tle for some, 0(n2)
#Brute force way is to consider each index as starting point and see till where u can go
    #   n = len(fruits)
    #     maxlen = 0

    #     # Try every starting index i
    #     for i in range(n):
    #         freq = {}
    #         # Extend j to the right as far as possible
    #         for j in range(i, n):
    #             f = fruits[j]
    #             freq[f] = freq.get(f, 0) + 1

    #             # If we have more than 2 types, stop extending
    #             if len(freq) > 2:
    #                 break

    #             # Valid window [i..j] with ≤ 2 types
    #             maxlen = max(maxlen, j - i + 1)

    #     return maxlen


#I try, This is all bogus, sorting wont work, we need to keep it in order
        # fruits.sort()
        # freq = {}
        # for i in range(len(fruits)):
        #     freq[fruits[i]] = 1+ freq.get(fruits[i],0)
        #     sortedfreq = sorted(freq, key=freq.get, reverse=True)
        #     max1 =  sortedfreq[0]
        #     max2 = sortedfreq[1]

        # return max1 * freq[max1] + max2 * freq[max2]


        

        