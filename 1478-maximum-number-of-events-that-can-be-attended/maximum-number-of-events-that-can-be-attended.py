class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        #priortise  smaller events while attending #so if wanna take min endtime , use minheap 
        #O(N log N), Space: O(N)
        events.sort(key = lambda x: x[0]) #sort by start needed
        heap = []

        i,day =0,1
        attended = 0
        #use while cause we need to skip days and i all too
        while i < len(events) or heap: #or heap so that u drain remaining events
            #If no available events, jump day to next event's start (avoid day-by-day loop)
            if not heap:
                day = events[i][0]

            # Add all events that start on/before 'day'
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i+=1

            # Remove events that already ended before 'day'
            while heap and heap[0] < day:
                heapq.heappop(heap)

            
            # Attend the event that ends earliest
            if heap:
                heapq.heappop(heap)
                attended+=1
                day+=1 #next day
        return attended

#Use a min-heap to track active events by their end days.

#---------------------------Bruet force, O(N * D), Space : O(D) -----------------------------------
# Try attending every event from its startDay to endDay and use the first available day not already used.
# def maxEvents(events):
#     events.sort()
#     used = [False] * 100001
#     count = 0
#     for s, e in events:
#         for d in range(s, e + 1):
#             if not used[d]:
#                 used[d] = True
#                 count += 1
#                 break
#     return count

#----- why think of heap?----------------------------------------------
# Think of it as a scheduling game where each day you’re allowed to pick at most one “still-available” event.

# The greedy rule that works is:
# On each day, among all events that have started (start ≤ day) and not yet expired (end ≥ day), attend the one that ends earliest.

# Heap mental model
# Sort events by startDay.# Sweep day forward.
# Maintain a min-heap of endDays for events that have started.
# Each day:
# 1)Push into heap all events with startDay == day (or <= day as you advance).
# 2)Pop expired events (end < day).
#3) If heap not empty: pop one (the smallest end) → attend it today.

# If you attend any available event today, and you picked one that ends later than another available one, swapping to the earlier-ending event can’t reduce future options (it frees more days later). So “earliest end” is always safe.

#-------------------My aprroach!, works but Tle last 3 cases ----------------------------
        # events.sort(key = lambda x: x[0]) #sort start times
        # events.sort(key = lambda x: x[1]) #this needed for it!!!
        # attended = 0
        # busydays = []
        # for e in events:
        #     day = e[0]
        #     while  e[0] <= day <= e[1]:
        #         if day not in busydays:
        #             busydays.append(day)
        #             attended+=1
        #             break
        #         day+=1
        # return attended

# ------------------------    Test cases --------------------------

# I just have one advice: Make a habit of coming up with your own edge cases

# Input: events = [[1, 10], [1, 10], [1, 10], [1, 10]]
# Output: 4
#Explanation: All events overlap entirely. You can attend each event on a different day within the range.

# Input: events = [[1, 2], [2, 2], [1, 2], [1, 2]]
# Output: 2
# Explanation: Multiple events end on the same day. You can only attend two of them.

# Input: events = [[1, 100], [50, 100], [60, 70], [90, 95]]
# Output: 4
# Explanation: Despite the large range, you can still attend all events. Attend each on the earliest possible day.

#-----------How to appoach soln?  -------------------------------------------

# Intuition
# Imagine you're trying to attend as many events as possible, but each event only happens on a specific range of days like from day 1 to day 3. You can attend only one event per day. To get the most events, you want to always pick the event that ends soonest, so you don’t miss out on it. That’s because if you skip an event that ends early, you may not get another chance later, while events with longer ranges can still be attended on future days. So, for each day, we keep track of which events are available and always attend the one that ends the earliest.

# Tiny walkthrough
# Events: [[1,2],[1,3],[2,2]]
# Sorted by start: [[1,2],[1,3],[2,2]]
# day = 1, i=0
# add events with start ≤ 1:
# push end 2 (i=1)
# push end 3 (i=2)
# heap has [2,3] → attend the one ending earliest (2)
# day = 2, i=2
# add events with start ≤ 2:
# push end 2 (i=3)
# heap has [2,3] (plus we pop expired ones if any)
# attend end 2
# That’s it: the loop is just making sure the heap contains all events that are “open” by today.


