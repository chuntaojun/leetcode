class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng = len(s)
        dp = [[0]*leng for i in range(leng)]
        for j in range(leng):
            dp[j][j] = 1
            for i in range(j - 1, -1, 1):
                if s[i] != s[j]:
                    dp[i][j]=dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                elif s[i] == s[j]:
                    dp[i][j]+=dp[i+1][j] + dp[i][j-1]+1
        return dp[0][leng - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("aaa"))
    
