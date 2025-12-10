class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)#we cant loop over string
        firstnonine, firstnonzero ='9','0' #initialiase as string!!
        for i in range(len(num)):
            if num[i] != '9':
                firstnonine = num[i]
                break
        for i in range(len(num)):
            if num[i] !='0':
                firstnonzero = num[i]
                break

        maxnum =int(num.replace(firstnonine, '9'))
        minnum = int(num.replace(firstnonzero, '0'))

        return maxnum - minnum

#Try to remap the first non-nine digit to 9 to obtain the maximum number.
#Try to remap the first non-zero digit to 0 to obtain the minimum number.

#maxnum = num ## is wrong, if we do this, they both point at same
# maxnum[i] = '9' # also wrong, string cant mutate