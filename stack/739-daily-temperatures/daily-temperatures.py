class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Make use of monotonic stack for such problems
        #stack where u in some way keep it structly increasing or decreasing
        res = [0]*len(temperatures)
        stack = [] #[(num,index)]
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]: #while not if
                lasttemp, index = stack.pop()
                res[index] =  i - index
    
            stack.append((temperatures[i],i)) #have to do in any case
        return res



#note- sorting wont work, since we need index

#res = [] and then doing  res[i] = j give error
# res is an empty list; assigning with res[i] = ... gives IndexError!!

#Brute force works but some cases TLE
        # res = [0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j-i #!!!The problem wants number of days to wait, not the index of the warmer day.
        #             break
        # return res
