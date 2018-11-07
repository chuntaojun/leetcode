#
# [650] 2 Keys Keyboard
#
# https://leetcode-cn.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (33.98%)
# Total Accepted:    810
# Total Submissions: 2.4K
# Testcase Example:  '3'
#
# 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
# 
# 
# Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
# Paste (粘贴) : 你可以粘贴你上一次复制的字符。
# 
# 
# 给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
# 
# 示例 1:
# 
# 
# 输入: 3
# 输出: 3
# 解释:
# 最初, 我们只有一个字符 'A'。
# 第 1 步, 我们使用 Copy All 操作。
# 第 2 步, 我们使用 Paste 操作来获得 'AA'。
# 第 3 步, 我们使用 Paste 操作来获得 'AAA'。
# 
# 
# 说明:
# 
# 
# n 的取值范围是 [1, 1000] 。
# 
# 
#
import math

class Solution:

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if self.isPrime(n):
            return n
        dp = [0 for i in range(n + 4)]
        dp[1] = 0; dp[2] = 2; dp[3] = 3; dp[5] = 5
        for i in range(3, n + 1):
            a, b = self.get_max_factor(i)
            if a == 0 and b == 0:
                dp[i] = i
                continue
            # print("a is :" + str(a) + ", b is :" + str(b) + '\n')
            dp[i] = dp[a] + b
        print(dp)        
        return dp[n]

    def isPrime(self, a):
        b = int(math.sqrt(a)) + 1
        for i in range(2, b + 1):
            if a % i == 0:
                return False
        return True

    def get_max_factor(self, a):
        for i in range(int(a / 2) + 1, 1, -1):
            if a % i == 0:
                return i, int(a / i)
        return 0, 0


if __name__ == '__main__':
    s = Solution()
    s.minSteps(512)
