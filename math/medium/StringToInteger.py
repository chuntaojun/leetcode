class Solution(object):
    def myAtoi(self, strs):
        ans = 0
        INT_MAX, INT_MIN = 2147483647, -2147483647
        ans = 0
        sign = 1
        i = 0
        # 过滤前导空格
        while i < len(strs) and strs[i].isspace():
            i += 1
        if i < len(strs) and strs[i] == '-':
            sign = -1
        if i < len(strs) and (strs[i] == '-' or strs[i] == '+'):
            i += 1
        # 过滤前导空格后进行数字的判断，如果不是，直接输出结果
        while i < len(strs) and strs[i].isdigit():
            digit = int(strs[i])
            if INT_MAX / 10 >= ans:
                ans *= 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= ans:
                ans += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return ans * sign
