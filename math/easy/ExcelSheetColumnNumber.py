class Solution(object):
    def titleToNumber(self, s):
        sum = 0
        for i in range(len(s)):
            temp = ord(s[i]) - 65 + 1
            sum = 26 * sum + temp
        return sum


# 输入一个26进制的数，将其转换为10进制的数