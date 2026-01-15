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
        x = (a - 1) * 7 + b
        while x > 40:
            a = rand7()
            b = rand7()
            x = (a - 1) * 7 + b

        #Modulo gives 0..9, so you “shift” it to 1..10.
        return (x % 10) + 1

        

# You come up with it by following one mental rule:
# If you want uniform output, start from a uniform “bucket of equally-likely states”, then map buckets evenly. If it doesn’t divide evenly, reject the leftovers.

# Build a uniform integer 1..49 from two independent rand7() calls.
# Think of (a, b) as a coordinate in a 7x7 grid:
#   a in {1..7} chooses the row, b in {1..7} chooses the column.
# Convert that 2D coordinate to a 1D index:
#   (a-1) makes rows 0..6, multiply by 7 to shift by full rows,
#   then add b (1..7) for the column position.
# Result: x ranges 1..49, and each value occurs with probability 1/49.
# x = (a - 1) * 7 + b

# The main idea is when you generate a number in the desired range, output that number immediately. If the number is out of the desired range, reject it and re-sample again. As each number in the desired range has the same probability of being chosen, a uniform distribution is produced.


#---- My first wrong answer--------------------
#     return (rand7() + rand7()) % 11
# - wrong cause some numbers more likely to be picked

