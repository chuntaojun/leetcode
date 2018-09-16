# -*- coding: UTF-8 -*-
"""
iven a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

找到每一个数字特有的字母，根据特有的字母进行计算数字的个数

"""


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        ans, temp = [], {}
        temp[0] = s.count('z')
        temp[2] = s.count('w')
        temp[6] = s.count('x')
        temp[7] = s.count('s')
        temp[8] = s.count('g')
        temp[4] = s.count('u')
        temp[5] = s.count('f')
        temp[3] = s.count('h')
        temp[9] = s.count('i')
        temp[1] = s.count('o')

        temp[7] -= temp[6]
        temp[5] -= temp[4]
        temp[3] -= temp[8]
        temp[9] = temp[9] - temp[8] - temp[5] - temp[6]
        temp[1] = temp[1] - temp[0] - temp[2] - temp[4]
        for i in range(10):
            for j in range(temp[i]):
                ans.append(i)
        return "".join(map(str, ans))


if __name__ == '__main__':
    s = Solution()
    print s.originalDigits("zeroonetwothreefourfivesixseveneightnine")
