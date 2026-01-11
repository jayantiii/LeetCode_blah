class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        kstr = ""
        for i in range(len(s)-1,-1,-1):
            if s[i] == "-":
                continue 

            # add current char first (uppercase) - not in a if condn
            kstr = s[i].upper() + kstr

            # if group complete, push it
            if len(kstr) == k:
                res.append( kstr)
                kstr = ""

        #the first group
        if kstr:
            res.append(kstr)

        return "-".join(reversed(res)) # reverse needed
        # just do, "-".join() , dont try to append "-" in each loop

#-----------------------Cleaner -------------------------------------
#avoid the “leftover after loop” block by writing directly into the output while scanning from the end.

        # out = []
        # cnt = 0

        # for i in range(len(s) - 1, -1, -1):
        #     ch = s[i]
        #     if ch == "-":
        #         continue

        #     if cnt == k:
        #         out.append("-")
        #         cnt = 0

        #     out.append(ch.upper())
        #     cnt += 1

        # out.reverse()
        # return "".join(out)

            


        