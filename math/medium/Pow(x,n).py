class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.testPow(x, abs(n))
        elif n == 0:
            return 1
        return self.testPow(x, n)

    def testPow(self, x, n):
        if n == 1:
            return x
        temp = self.myPow(x, n >> 1)
        if n & 1 != 0:
            result = x * temp * temp
        else:
            result = temp * temp
        return result