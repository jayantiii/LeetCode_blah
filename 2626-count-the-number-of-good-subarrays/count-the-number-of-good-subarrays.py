class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        hashmap = {} #number: freq
        kval = 0
        l = 0
        n = len(nums)
        goodsub = 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            
            else: #its there        
                hashmap[nums[i]] +=1
                pairs = hashmap[nums[i]] -1 
                kval+=pairs #add pairs and not +1
                while kval >= k: #use while and not if
                    hashmap[nums[l]] -=1
                    kval -= hashmap[nums[l]] #reduce the pair
                    l+=1 
                    goodsub += n - i #array before i

        return goodsub

# #good subarray
# #- (i,j) i<j and arr[i] == a[j]
# # nums = [5,2,3,1,4,3,2,2,4], k = 1 , 7-3 = 4
#          3:1 -->  +1 = 2, total 2-1 = 2 , num
#          1:1
#          4:1
    

