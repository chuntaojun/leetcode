import math


class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        if n == 0:
            return False
        while n != 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True


# 对数处理法
def LogFun(n):
    if math.log(n, 3) - int(math.log(n, 3)) == 0:
        return True
    return False


s = Solution()
print s.isPowerOfThree(15)
