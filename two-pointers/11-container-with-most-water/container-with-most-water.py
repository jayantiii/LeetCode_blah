class Solution:
    def maxArea(self, height: List[int]) -> int:
        #use 2 pointer pattern
        l,r = 0, len(height) -1
        maxarea = 0
        while l <r:
            maxarea = max(maxarea,min(height[l],height[r])*(r-l))
         #Note -  pointer move dont depend on arealr >maxarea:
         #Imp to know when to move pointer
            if height[l] > height[r]:
                r-=1  #its r-=1, dont confuse and do+1
            else:
                l+=1
        return maxarea

#bruteforce works, but tle for last cases
        # maxarea = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area = min(height[i],height[j]) * (j-i)    --- main!!
        #         maxarea = max(maxarea, area)

        # return maxarea

        