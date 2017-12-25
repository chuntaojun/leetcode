class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        return sqrt(1, x / 2, x)


def sqrt(left, right, x):
    mid = (left + right) / 2
    if mid * mid < x < (mid + 1) * (mid + 1):
        return mid
    elif mid * mid > x:
        return sqrt(left, mid - 1, x)
    elif mid * mid < x:
        return sqrt(mid + 1, right, x)
    return mid
