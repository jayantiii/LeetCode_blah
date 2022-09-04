https://www.youtube.com/watch?v=fMSJSS7eO1w - see, tricky logic
​
**#other soln**
#noticing that the first element of the last row of the input is the first element of the first row of the output, the second element of the last row of the input is the first element of the second row of the output etc. thus
​
n = len(matrix)
for row in matrix[::-1]:
for i in range(n):
element = row.pop(0)
matrix[i].append(element)