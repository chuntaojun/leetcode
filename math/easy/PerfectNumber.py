import math


class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 0 or num == 1:
            return False
        mid = int(math.sqrt(num))
        sums = 1
        for i in range(2, mid + 1):
            if num % i == 0:
                sums += i + num / i
                if sums > num:
                    return False
        if sums == num:
            return True
        else:
            return False
