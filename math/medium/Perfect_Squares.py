class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import sys
        if n == 1:
            return 1
        dp = [0]
        while len(dp) <= n:
            i = len(dp); j = 1
            perfect_num = sys.maxsize
            while (j * j <= i):
                perfect_num = min(perfect_num, dp[i - j * j] + 1)
                j += 1
            dp.append(perfect_num)
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))

