# coding=utf-8
"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 10
        if n == 0:
            return 1
        sums, temp = 10, 9
        for i in range(2, n + 1):
            for j in range(9, 9 - i + 1, -1):
                temp *= j
            sums += temp
            temp = 9
        return sums


if __name__ == '__main__':
    s = Solution()
    print s.countNumbersWithUniqueDigits(5)
