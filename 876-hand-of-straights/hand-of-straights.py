class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
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

# Also, you never remove cards with 0 count from cardcount, so min(cardcount.keys()) may pick a card that’s already used up, which will cause a False result or KeyError in some cases.
        