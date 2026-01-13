class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))

        

        
#Myapproach - passed nly few cases (failed eg --"aab "baa", output shld be true but came false)
#         b = len(magazine)
#         if a > b : return False
#         i,j = 0,0
#         while(a > i and b > j):
#             if ransomNote[i] == magazine[j]:
#                 i=i+1
#             j=j+1
#         print(i,a)
           
#         return i==a)     
        
#         a = len(ransomNote)
#         b = len(magazine)
#         if a > b : return False
#         i,j = 0,0
#         while(a > i and b > j):
#             if ransomNote[i] == magazine[j]:
#                 i=i+1
#             j=j+1
#         print(i,a)
           
#         return i==a
                
     

    