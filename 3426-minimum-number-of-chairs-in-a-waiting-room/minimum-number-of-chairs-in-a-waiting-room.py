class Solution:
    def minimumChairs(self, s: str) -> int:
        minchairs = 0
        people = 0 #inroom
        for i in range(len(s)):
            if s[i] == "E":
                if people >= minchairs:
                    minchairs +=1
                people +=1
            else:
                people -=1
        return minchairs
        

#My first answer!! - one logic flaw, cant just simply -=1
#cause if we have used a chair means we add ot count, cant just do -=1

        # minchair = 0
        # for i in range(len(s)):
        #     if s[i] == "E":
        #         minchair +=1
        #     else:
        #         minchair -=1
        # return minchair
        