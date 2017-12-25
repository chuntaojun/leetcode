"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = divisor < 0 < dividend or dividend < 0 < divisor
        dividend, divisor = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if dividend >= divisor << shift:
                dividend -= divisor << shift
                ans += 1 << shift
            shift -= 1
        if neg:
            return ans * -1
        if ans >= INT_MAX:
            return INT_MAX
        return ans


s = Solution()
print s.divide(100, 3)
