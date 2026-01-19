# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()
        x = (a - 1) * 7 + b #2d grip map to numbers
        while x > 40:
            a = rand7()
            b = rand7()
            x = (a - 1) * 7 + b

        #Modulo gives 0..9, so you “shift” it to 1..10.
        return (x % 10) + 1

        

# You come up with it by following one mental rule:
# If you want uniform output, start from a uniform “bucket of equally-likely states”, then map buckets evenly. If it doesn’t divide evenly, reject the leftovers.

# Map 2D (row=a, col=b) in a 7x7 grid to a unique 1D index x in [1..49]:
# - Each row has 7 cells.
# - Rows before a contribute (a-1)*7 cells.
# - Then add b (1..7) to land inside row a.
# So:
#   row 1 -> 1..7
#   row 2 -> 8..14
#   row 3 -> 15..21
#   ...
#   row 7 -> 43..49
# x = (a - 1) * 7 + b


# The main idea is when you generate a number in the desired range, output that number immediately. If the number is out of the desired range, reject it and re-sample again. As each number in the desired range has the same probability of being chosen, a uniform distribution is produced.


#---- My first wrong answer--------------------
#     return (rand7() + rand7()) % 11
# - wrong cause some numbers more likely to be picked

