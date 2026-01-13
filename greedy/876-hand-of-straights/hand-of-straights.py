class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #O(n²) - cause of  min(cardcount.keys()) this line
        if len(hand) % groupSize != 0:
            return False
        numberofgroups = len(hand) // groupSize
        cardcount = {}
        for i in range(len(hand)):
            #Dont do  cardcount -> overwrites the whole dictionary
            cardcount[hand[i]] = cardcount.get(hand[i],0) + 1 
     
        while numberofgroups:
            smallest = min(cardcount.keys()) #keys not values
            for i in range(smallest, smallest+ groupSize): #ranges see
                if cardcount.get(i, 0) == 0: # Use get to avoid KeyError
                    return False
                cardcount[i] -=1
                if cardcount[i] == 0:
                    del cardcount[i]  # Remove used-up cards

            numberofgroups -=1

        return True
            


#Idea
#Always find the smallest value and try to make a sequence and keep repeating

#0ne mistake i did
# Also, you never remove cards with 0 count from cardcount, so min(cardcount.keys()) may pick a card that’s already used up, which will cause a False result or KeyError in some cases.

#-------------------Interview------------------------
# “A simple brute-force approach would be: sort the hand, then try to repeatedly take the smallest remaining card and see if the next groupSize - 1 consecutive cards exist. If at any step we can’t form a consecutive group, return False.” So overall time ≈ O(n log n + n * groupSize)

# “To avoid repeatedly scanning the whole list, we can count the number of each card using a dictionary (or Counter). Then, we always pick the smallest available card, and decrease the count of it and the next groupSize - 1 consecutive cards. If any of the consecutive cards don’t exist, return False. Continue this until all cards are used.”

#------mORE optimised using minheap, O(n log n)---------------------
        # if len(hand) % groupSize != 0:
        #     return False
        
        # # Count how many of each card we have
        # cardcount = Counter(hand)
        
        # # Create a min-heap of all distinct cards
        # heap = list(cardcount.keys())
        # heapq.heapify(heap)
        
        # while heap:
        #     smallest = heap[0]  # get the smallest card
        #     for i in range(smallest, smallest + groupSize):
        #         if cardcount.get(i, 0) == 0:
        #             return False
        #         cardcount[i] -= 1
        #         if cardcount[i] == 0:
        #             # Remove card from heap if its count reaches 0
        #             # Only remove if i is the smallest in heap
        #             if i == heap[0]:
        #                 heapq.heappop(heap)
        # return True
        