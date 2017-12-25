class Solution(object):
    def addDigits(self, num):
        if num <= 9:
            return num
        if num % 9 == 0:
            return 9
        n = num / 9
        return num - 9 * n
