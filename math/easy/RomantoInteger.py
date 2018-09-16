class Solution(object):
    def romanToInt(self, s):
        ans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            temp = ans[s[i]]
            if i == len(s) - 1 or ans[s[i + 1]] <= ans[s[i]]:
                num += temp
            else:
                num -= temp
        return num


s = Solution()
print s.romanToInt("CCVIII")
