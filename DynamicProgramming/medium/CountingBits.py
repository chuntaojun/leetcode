class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]
        for i in range(1, num + 1):
            dp.append(dp[i & (i - 1)] + 1)
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(64))
    
