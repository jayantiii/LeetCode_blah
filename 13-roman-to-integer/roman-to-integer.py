class Solution:
    def romanToInt(self, s: str) -> int:
    #Hint: Problem is simpler to solve by working the string from back to front and using a map.
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s) -1
        finalnumber = 0
        while n >= 0: #start reverse
            char = roman[s[n]] #take actual int value
            # Check if there is a previous character to compare 
            if n > 0:
                prevchar = roman[s[n-1]]
                if prevchar < char: #subtractive case
                    number =  char - prevchar
                    n = n-2 #cause took 2 chars
                else:
                    number = char
                    n = n-1
            else:
                number = char
                n = n-1

            finalnumber = finalnumber + number

        return finalnumber

## IMPPP -logic would be to handle the subtractive cases where a smaller value precedes a larger value (e.g., IV = 4,)!!

#Roman numerals are not positional, so multiplying by 10s, 100s makes no sense. we dont need anything like place or something

#Simpler, cleaner solution
    # def romanToInt(self, s: str) -> int:
    #     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     total, prev = 0, 0
    #     for ch in reversed(s):
    #         val = roman[ch]
    #         total += -val if val < prev else val
    #         prev = val
    #     return total

        