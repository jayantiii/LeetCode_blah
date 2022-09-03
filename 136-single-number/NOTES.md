# 0(n)
we can use a hashset where , we keep adding elements and remove them wen they occur again. This way at the last only one element will be left in the hashset who doesnt have a duplicate.
**#best soln** -- use constant space - by bit manipulation (xor)
---> n xor 0 = n ( always)
so we will xor all elements together of array and result will be the one who doesnt have a duplicate. because numbers having duplicate will get cancelled out (i.e 000) wen xoring.
https://www.youtube.com/watch?v=qMPX1AOa83k