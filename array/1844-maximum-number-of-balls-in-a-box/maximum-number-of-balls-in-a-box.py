class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        n = highLimit - lowLimit + 1 #no. of balls
        maxballs = 0
        mapper = {}

        for num in range(lowLimit, highLimit+1):
            #find sum ofnumber!!
            sum = 0
            while num:
                digit = num % 10 
                sum += digit
                num = num // 10 #remove the last digit

            mapper[sum] = mapper.get(sum,0) + 1
    
        for v in mapper.values():
            maxballs = max(maxballs, v)
        return maxballs

#Yes — while num: stops when num becomes 0 because Python treats the condition as a truthiness check.

            

            
        