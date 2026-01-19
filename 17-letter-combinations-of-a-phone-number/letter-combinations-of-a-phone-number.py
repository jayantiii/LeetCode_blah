class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = []
        maps = {2: "abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs", 8:"tuv"
                    , 9:"wxyz"}

        def backtrack(i,currcomb):
            if i == len(digits):
                comb.append(currcomb)
                return

            string = maps[int(digits[i])]
            for char in string:
                backtrack(i+1,currcomb + char)
           
        backtrack(0,"")
        return comb

#One Imp Mistake!!
# i didnt do for loop inside assuming that all strings are 3 leters so i can just call 3times but # failed to notice some are 4 letters also
        