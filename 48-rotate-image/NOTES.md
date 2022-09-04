**#Simpler**
#transpose
for row in range(len(matrix)):
for col in range(row,len(matrix)):
temp = matrix[row][col]
matrix[row][col] = matrix[col][row]
matrix[col][row] = temp
​
#reverse
for row in matrix:
row.reverse()
#
#noticing that the firs element of the last row of the input is the first element of the first row of the output, the second element of the last row of the input is the first element of the second row of the output etc. thus
​
n = len(matrix)
for row in matrix[::-1]:
for i in range(n):
element = row.pop(0)
matrix[i].append(element)