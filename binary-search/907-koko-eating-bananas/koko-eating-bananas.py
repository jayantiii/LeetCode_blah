class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        kmax = max(piles) #k doesnt need to me more than this

        def caneatall(k,h):
            hoursneeded = 0
            for p in piles:
                hoursneeded += ceil(p / k) # cause round up hours

            if hoursneeded > h:
                return False
            return True

        #Binary search the range --
        l,r = 1,kmax
        while l <=r:
            mid = (l+r)//2
            if caneatall(mid,h):
                r = mid -1
            else:
                l = mid+1

        return l # return l or can return r

#Observation
# piles.length should be less than or equal to h
# cause each hour , only 1 pile can. be eaten

# Mental model (why binary search works)
# As k increases, required hours sum(ceil(p/k)) never increases → monotonic predicate → binary search applies.

#Note - Use integer ceil without floats: (p + k - 1) // k (no need ceil()).

#-------------------My mistakes--------------------
#calc pile wise p/k and not like below all at once
#This is wrong
#    def caneatall(k,h)
#             hoursneeded = totalsum //k
#             if hoursneeded > h:
#                 return false
#             return True
#not how this problem works, because Koko can only eat from one pile per hour, and if a pile has p bananas it takes ceil(p/k) hours for that pile.

#start range from 1
#kmin = min(piles) is wrong. k can be 1 (slow), you just might need more hours.