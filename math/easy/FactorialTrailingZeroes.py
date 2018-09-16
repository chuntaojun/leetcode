class Solution(object):
    def trailingZeroes(self, n):
        temp = 0
        while n:
            temp += n / 5
            n /= 5
        return temp


s = Solution()
print s.trailingZeroes(352) * 10
