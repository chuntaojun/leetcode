"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = [str(numerator / denominator)]
        temp = {}
        numerator -= denominator * (numerator / denominator)
        if numerator == 0:
            return ''.join(ans)
        elif numerator < denominator:
            ans.append('.')
            while numerator % denominator == 0:
                numerator *= 10
                a = numerator / denominator
                ans.append(str(a))
                if temp.get(a) != numerator % denominator:
                    temp[a] = numerator % denominator
                else:
                    pass
                numerator -= denominator * a


if __name__ == '__main__':
    pass
