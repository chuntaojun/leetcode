import math


class Solution(object):
    def judgeSquareSum(self, c):
        mid = int(math.sqrt(c))
        for i in range(mid + 1):
            b = math.sqrt(c - i * i)
            if b == int(b):
                return True
        return False
