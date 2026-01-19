class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(website)
        info = sorted(zip(timestamp,website, username)) #sort by timestamp

        uservisits = defaultdict(list) #Find all websites for user
        for _, w,u in info:
            uservisits[u].append(w)

        #Create all distinct patterns possible for len3 adn count
        patterns = defaultdict(int) # default 0
        for _, user in uservisits.items():
            seen = set() #IMP -each user should contribute at most 1 to any given pattern.

            for i in range(len(user)-2):
                for j in range(i+1, len(user)-1):
                    for k in range(j+1, len(user)):
                        one = user[i]
                        two = user[j]
                        three = user[k]

                        if (one,two,three) in seen:
                            continue
                        seen.add((one,two,three))
                        patterns[(one,two,three)] +=1 


        #find the highest count pattern
        bestp = None # is tuple
        score = -1
        for p,c in patterns.items():
            if score == -1: #handle this case
                bestp, score = p, c
                continue
            if c > score:
                bestp = p
                score = c
            elif c == score:
                bestp = p if p < bestp else bestp #lexographically

        return list(bestp)
    


#Let's find for every user separately the websites he visited.
#A pattern is a list of three websites (not necessarily distinct).

