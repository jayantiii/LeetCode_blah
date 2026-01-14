class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False

        g = 0  # gcd accumulator, math.gcd(0, n) returns abs(n).
        for v in Counter(deck).values():
            g = gcd(g, v)# keep only common divisor across counts

        return g >= 2 #group size X ≥ 2

#See this example before solving
# deck = # [1,1,2,2,2,2]
# Expected # true

#---------My wrong answer-----------------------------
#  This is not enough --> v % prev != 0, we need to take gcd
# counts = [4, 6] min = 4
# your check: 6 % 4 != 0 → returns False

        # count = Counter(deck)
        # prev = min(count.values()) # take minimum 
        # for k,v in count.items():

        #     if  v % prev != 0:
        #         return False

        # return True
        