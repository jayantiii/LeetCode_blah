class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks) #creates hashmap
        maxheap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxheap)
        queue = deque() #(element, nextime)
        time = 0

        while maxheap or queue:
            time+=1
            if maxheap:
                cnt = heapq.heappop(maxheap)*-1 #positive it
                cnt = cnt -1 #decrease one
                idletime = time+n #next time it can be used
                if cnt: #dont append if cnt zero
                    queue.append([cnt,idletime])

            if queue and queue[0][1] == time: #means next while loop it can be used
                cnt,idletime = queue.popleft()
                heapq.heappush(maxheap,cnt*-1) #push negative value
        return time


#Beter to process more frequent char first always
#Use max heap to continously figure which has most tasks left
#Use and max heap and queue - little difficult ot understand the process

#Max heap - will keep the highest number track
#once pop heap, decrease count and add to queue with the next time it can be used
#when the time t comes, add it max to maxheap and repeat process
        