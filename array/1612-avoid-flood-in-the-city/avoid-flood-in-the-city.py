class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        rainedlakes = set()
        lastrain = {} #UPDATE the day it rained in lake {lake:lastdayrain}
        drydays = []
        for day in range(0,len(rains)): #days
            if rains[day] > 0:

                if rains[day] in rainedlakes:
                    #if no day to dry left, then flood
                    if not drydays: return []

                    #binary search and find it, use lastrain
                    lake = rains[day]
                    lakelastrain = lastrain[lake]
                    dayindex = bisect_right(drydays,lakelastrain) # first dry day > lakelastrain

                    #Also, If all available dry days are <= lakelastrain, you must return [].
                    if dayindex == len(drydays):
                        return []  # no valid dry day available
                    dryday = drydays.pop(dayindex)
                    ans[dryday] = lake
                    rainedlakes.remove(rains[day]) #use remove for set
                    
                rainedlakes.add(rains[day])
                lastrain[rains[day]] = day
            #Choose to dry a lake
            else:
                drydays.append(day)
                ans[day] = 1 # dry days need to be set positibe number
        
        return ans

# “Choosing the earliest valid dry day is safe because it only reduces constraints for future events; choosing a later day could block a lake that has a tighter deadline.”
#-----------------Interview what to say -------------------------

# Your current list + bisect solution is fine for interviews as a first pass (clear idea, correct constraints), but you should explicitly say:

# “This is correct, but Python list deletion is O(n), so worst-case can degrade to O(n²).”
# “To make it truly optimal O(n log n), I’d use an ordered set / TreeSet (Treap/SortedList).”

# With an ordered set (TreeSet/Treap/SortedList): each operation is O(log n) ⇒ total O(n log n).
# With Python list + bisect + pop(i): selection is O(log n) but deletion is O(n) ⇒ worst-case O(n²).
        
#---------------Read full Q , Dont miss below points------------------
#- If it is impossible to avoid flood return an empty array.
#but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood

#So the main thing is to understand, when there is dry day how to choose which lake to dry
#What if some lake is gonna rain again in future, then we should choose that one to dry before

#A dry day is only valid for lake L if it is after the lake’s last rain day. Cosnider this also when coding
#So the missing piece in your logic is: you need last_rain[lake], and you must select the first dry day after last_rain[lake] (a lower_bound query).

#------Below is my first answer where i didnt consider above points at all -------
    #   ans = [-1 for i in range(len(rains))]
    #     rainedlakes = []
    #     for day in range(0,len(rains)): #days
    #         if rains[day] > 0:
    #             rainedlakes.append(rains[day])
    #         else: #Dry a lake
    #             ans[day] = rainedlakes.pop()
     
    #     return ans if not rainedlakes else []