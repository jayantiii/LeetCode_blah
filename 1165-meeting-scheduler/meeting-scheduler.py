class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        j = 0
        for s1,e1 in slots1:
            # skip slots2 that end before s1 starts
            while j < len(slots2) and slots2[j][1] < s1:
                j += 1

            # try overlapping slots2 starting from current j
            while j < len(slots2) and slots2[j][0] <= e1:

                s2, e2 = slots2[j][0], slots2[j][1]

                commontime = min(e1,e2) - max(s1,s2)
                if commontime >= duration: #found ans
                    #find the range
                    start = max(s1,s2)
                    end = start + duration
                    return [start,end]
            
                #dONT DIRECTLY DO J+=1
                # IMP! # discard the interval that ends earlier
                if e2 <= e1:
                    j += 1 #          # slots2 ends first -> move j
                else:
                    # slots1 ends first -> next s1
                    break
                        
        return []





#important to note that the slots are AVAILABILITY times of each person. I originally misinterpreted it as meeting times and was trying to find a gap between the slots instead of an intersection.

#What if there are n slots? How would you solve it?


 

 
