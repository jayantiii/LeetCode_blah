class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If only 1 row or string is too short, no zigzag possible
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows #store all rows in zig-zag
        direction = 1
        currrow = 0
        for char in s:
            rows[currrow] =  rows[currrow] + char
            # If we are at the top or bottom, we need to "bounce"
            if currrow == numRows -1:
                direction = -1 # Start moving up

            if currrow == 0:
                direction = 1 # Start moving down
            currrow += direction

        return "".join(rows)


# Instead of trying to calculate a complex mathematical formula for the index of each character, try simulating the process with a list of strings (one for each row):
# Track your current row.
# Track your current direction (e.g., +1 for down, -1 for up).
# Every time you reach the top row or the bottom row, flip your direction.