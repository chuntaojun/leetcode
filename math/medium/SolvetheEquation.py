"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-'
operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""


import re


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left_equal, right_equal = equation.split('=')
        left_fuhao, right_fuhao = [], []
        for i in range(len(left_equal)):
            if re.match('\+|-', left_equal[i]):
                left_fuhao.append(left_equal[i])
        for i in range(len(right_equal)):
            if re.match('\+|-', right_equal[i]):
                right_fuhao.append(right_equal[i])
        left_equal = re.split('\+|-', left_equal)
        right_equal = re.split('\+|-', right_equal)
        if left_equal.__contains__(''):
            left_equal.remove('')
        if right_equal.__contains__(''):
            right_equal.remove('')
        left_ans, right_ans = [0, 0], [0, 0]
        left_equal, left_ans, left_fuhao = self.fun(left_equal, left_ans, left_fuhao)
        right_equal, right_ans, right_fuhao = self.fun(right_equal, right_ans, right_fuhao)
        if left_ans[0] == right_ans[0] and left_ans[1] != right_ans[1]:
            return "No solution"
        if left_ans[0] == right_ans[0] and left_ans[1] == right_ans[1]:
            return "Infinite solutions"
        else:
            temp = (right_ans[1] - left_ans[1]) / (left_ans[0] - right_ans[0])
            return "x=" + str(temp)

    def fun(self, my_equal, ans, fuhao):
        temp = 1
        for i in range(len(my_equal)):
            if my_equal[i].__contains__('x'):
                a, b = my_equal[i].split('x')
                if len(my_equal) is len(fuhao):
                    if fuhao[i] is '-':
                        temp = -1
                else:
                    if i - 1 > 0:
                        if fuhao[i - 1] is '-':
                            temp = -1
                if a is not '':
                    ans[0] += int(a) * temp
                else:
                    ans[0] += 1 * temp
                temp = 1
            else:
                temp = 1
                if len(my_equal) is len(fuhao):
                    if fuhao[i - 1] == '-':
                        temp = -1
                else:
                    if i - 1 >= 0:
                        if fuhao[i - 1] is '-':
                            temp = -1
                ans[1] += int(my_equal[i]) * temp
                temp = 1
        return my_equal, ans, fuhao


if __name__ == '__main__':
    s = Solution()
    print s.solveEquation("x+5-3+x=6+x-2")
