class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        t = {}    #{name: [(city,time,ind),city,time,ind)..]} #store ind!!
        for i in range(len(transactions)):
            transaction = transactions[i].split(",")
            name = transaction[0]
            time = int(transaction[1])
            amount = transaction[2]
            city =  transaction[3]

            if int(amount) > 1000:
                invalid.add(i) #add indices
            #dont continue here, cause we need to check for previous invalid

            if name in t:
                oldtransac = t[name]
                for oldtc in oldtransac: #check all old!!
                    oldcity, oldtime,ind = oldtc
                    if abs(time - oldtime) <= 60 and city != oldcity:
                        invalid.add(i) #add indices in a set to prevent dup
                        invalid.add(ind) #rather than whole value, add indices!!!

            else: #newname
                t[name] = []

            t[name].append((city,int(time),i))

        return [transactions[i] for i in invalid]


# good question to ask : if the transactions are in the order they came in?
#if we need to makr previous seen tranc invalid

#Notice ( Run thrugh examples before code)
#if ["alice,20,800,mtv","alice,50,100,beijing"]
#-- Both 1 and 2 become invalid and not just 2

# if ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
#-- All 3 invalid here, not just last 2

##----MISTAKE------
# Keeping only the latest transaction per name is not enough because the rule is:
# A transaction is invalid if it has any other same-name transaction within 60 minutes in a different city — and both transactions become invalid.
# With t[name] = (city, time) you “forget” earlier transactions, so you can’t mark them invalid later.
            
        