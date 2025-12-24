class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        q.append(("0000",0)) #(state,turns)
        visit = set()
        def nextcombinations(lock,turns): #each digit can go up or down
            res = []
            for i in range(4):
                digit = int(lock[i])
                digitup = (digit +1)% 10  # cause we want 9 to turn to 0
                turnup = lock[:i] +  str(digitup)  + lock[i+1:]

                digitdown = (digit - 1 )% 10   # we want 0 to turn to 9 [ cause -1%10 is = 9]
                turndown = lock[:i] + str(digitdown) + lock[i+1:]

                if turnup not in deadends and  turnup not in visit:
                    res.append((turnup, turns+1))
                    visit.add(turnup)

                if turndown not in deadends and turndown not in visit:
                    res.append((turndown,turns+1))
                    visit.add(turndown)
            return res

        while q :
            lock, turns = q.popleft()
            if lock == target:
                return turns          
            children = nextcombinations(lock,turns)
            for child in children:
                q.append(child)
        return -1 


#one idea is to add deadends to visitset itself 
