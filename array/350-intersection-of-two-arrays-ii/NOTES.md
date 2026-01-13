**#Counter is unordered collection where elements and their respective count are stored as a dictionary. It implicitly creates a hash table of an iterable when invoked.**
**# elements() - when invoked on the Counter object will return an itertool of all the known elements in the Counter object.**
​
**##two pointers way:**
class Solution(object):
def intersect(self, nums1, nums2):
​
nums1, nums2 = sorted(nums1), sorted(nums2)
pt1 = pt2 = 0
res = []
​
while True:
try:
if nums1[pt1] > nums2[pt2]:
pt2 += 1
elif nums1[pt1] < nums2[pt2]:
pt1 += 1
else:
res.append(nums1[pt1])
pt1 += 1
pt2 += 1
except IndexError:
break
​
return res