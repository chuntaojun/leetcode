"""
Given a string representing an expression of fraction addition and subtraction,
you need to return the calculation result in string format.The final result
should be irreducible fraction. If your final result is an integer, say 2, you
need to change it to the format of fraction that has denominator 1. So in this
case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"
Example 3:
Input:"1/3-1/2"
Output: "-1/6"
Example 4:
Input:"5/3+1/3"
Output: "2/1"
"""


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        a, number, m, d = 1, 0, 0, 0
        molecular = {}
        denominator = {}
        for i in range(len(expression)):
            if expression[i] == '-' and i == 0:
                a = -1
            elif expression[i] == '-' and i != 0:
                denominator[d] = a * number
                d += 1
                number = 0
                a = -1
            elif expression[i] == '/':
                molecular[m] = a * number
                number = 0
                m += 1
                a = 1
            elif expression[i] == '+':
                a = 1
                denominator[d] = a * number
                number = 0
                d += 1
            else:
                number = number * 10 + int(expression[i])
                if i == len(expression) - 1:
                    denominator[d] = number
        de, mo = 1, 0
        for i in denominator:
            de *= denominator[i]
        for i in molecular:
            mo += molecular[i] * de / denominator[i]
        print mo, de
        print molecular, denominator
        if mo % de == 0:
            return str(mo / de) + "/1"
        elif de % mo == 0:
            if mo < 0:
                return str(-1) + "/" + str(de / abs(mo))
            else:
                return str(1) + "/" + str(de / mo)
        else:
            temp = abs(self.MaxCommonfactor(de, mo))
            return str(mo / temp) + "/" + str(de / temp)

    def MaxCommonfactor(self, n, m):
        while m != 0:
            temp = m
            m = n % m
            n = temp
        return n


if __name__ == '__main__':
    s = Solution()
    print s.fractionAddition("-4/7-3/4+2/3")
