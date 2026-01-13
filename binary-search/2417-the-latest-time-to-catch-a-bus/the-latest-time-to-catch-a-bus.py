from typing import List
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pset = set(passengers)

        currinbus = 0
        i = 0
        lastboarded = -1
        seatslast = 0 # needed!!
        for j in range(len(buses)):
            depart = buses[j]
            #simulate passengers boasrding bus!!
            while i < len(passengers) and passengers[i] <= depart and capacity > currinbus:
                lastboarded = passengers[i]
                currinbus +=1
                i+=1

            if j == len(buses) -1:
                seatslast = currinbus # save last bus fill count

            currinbus = 0 #reset

        # best candidate time before removing collisions
        if seatslast < capacity:
            t = buses[-1] #lastbus
        else:
            t = lastboarded - 1 # is  latest time you can arrive when last bus is full.

        # must not equal any passenger arrival time
        while t in pset:
            t -= 1

        return t

#To get the latest time you can arrive, you only need to think about the last bus (everything earlier just affects who’s still waiting).

#You might end up riding the second-last bus, but the latest arrival time is still determined by the last bus.

# That while loop is doing the actual boarding simulation, and it gives you the only two facts you need to compute the latest possible arrival time:
# Is the last bus full? (seats == capacity)
# If it’s full, what’s the cutoff passenger time? (last_boarded)

##“Last boarded” = the passenger who took the last seat on that bus (specifically, on the last bus after simulation).



            


        