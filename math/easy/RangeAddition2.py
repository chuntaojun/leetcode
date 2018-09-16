class Solution(object):
    def maxCount(self, m, n, ops):
        minX, minY = m, n
        if len(ops) == 0:
            return m * n
        for array in ops:
            if array[0] <= minX:
                minX = array[0]
            if array[1] <= minY:
                minY = array[1]
        return minY * minX
