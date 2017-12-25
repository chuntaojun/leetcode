class Solution(object):
    def convertToTitle(self, n):
        ans = ''
        while n:
            ans = str(chr((n - 1) % 26 + 65)) + ans
            n = (n - 1) / 26
        return ans


s = Solution()
print s.convertToTitle(1)


# 10进制转为26进制