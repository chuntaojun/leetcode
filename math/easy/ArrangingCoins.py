# 二分法去逼近一个接近得位置，让后进行判断


class Solution(object):
    def arrangeCoins(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) / 2
            if Sums(mid) < n:
                if n - Sums(mid) < mid + 1:
                    return mid
                else:
                    left = mid + 1
            elif Sums(mid) > n:
                if Sums(mid) - n < mid:
                    return mid - 1
                else:
                    right = mid - 1
            else:
                return mid
        return n


def Sums(n):
    return n * (n + 1) / 2
