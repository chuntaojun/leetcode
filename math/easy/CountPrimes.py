import math


# 高效素数打表法
class Solution(object):
    def countPrimes(self, n):
        ans = [True for i in range(1, n + 2, 1)]
        num = int(math.sqrt(n))
        for i in range(2, num + 1):
            for j in range(i + i, n + 1, i):
                ans[j] = False
        count = 0
        for i in range(2, n, 1):
            if ans[i]:
                count += 1
        return count
