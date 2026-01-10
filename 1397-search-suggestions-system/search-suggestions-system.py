class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res= []
        products.sort()
        l,r = 0,len(products) -1
        for i in range(len(searchWord)):
            ch = searchWord[i]
            # shrink left bound until it matches prefix[0..i]
            while l <= r and (len(products[l]) <= i or products[l][i] != ch):
                l += 1

            # shrink right bound until it matches prefix[0..i]
            while l <= r and (len(products[r]) <= i or products[r][i] != ch):
                r -= 1

            #get top 3
            j = l
            top3 = []
            k = 0
            while k< 3 and j<=r:
                top3.append(products[j])
                j+=1
                k+=1

            res.append(top3)

        return res

# Sort products, then keep a shrinking window [l, r] of strings that match the current prefix. For each new character i, advance l while products[l] is too short or mismatches at i, and similarly decrement r while products[r] mismatches. The first up to 3 items from products[l : l+3] are the suggestions for that prefix.

#Dont do only  -->while l <=r  --> can loop forever!!

#-------------------Binary Search, O(nlog(n))+O(mlog(n))---------------------------
# Since the question asks for the result in a sorted order, let's start with sorting products.
# An advantage that comes with sorting is Binary Search, we can binary search for the prefix. Once we locate the first match of prefix, all we need to do is to add the next 3 words into the result (if there are any), since we sorted the words beforehand.`

#  products.sort()
#         res = []
#         prefix = ""

#         for ch in searchWord:
#             prefix += ch

#             # leftmost position where `prefix` could be inserted
#             start = bisect.bisect_left(products, prefix)

#             top3 = []
#             for i in range(start, min(start + 3, len(products))):
#                 if products[i].startswith(prefix):
#                     top3.append(products[i])
#                 else:
#                     break
#             res.append(top3)

#         return res

#------------------------My mistake-----------------------------------
#Below is mistake cause while l <=r can loop forever!! do 2 seperate while loops

#  while l <=r:
#                 if len(products[l]) < i or  products[l][i] != ch:
#                     l+=1

#                 if len(products[r]) < i or products[r][i] !=ch:
#                     r-=1

        