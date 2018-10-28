#
# [72] Edit Distance
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (43.46%)
# Total Accepted:    2.2K
# Total Submissions: 5K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 示例 1:
# 
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释: 
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2:
# 
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释: 
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
#
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_s1 = len(word1)
        len_s2 = len(word2)
        dp = [[0 for i in range(len_s2 + 1)] for j in range(len_s1 + 1)]
        for i in range(len_s1 + 1):
            dp[i][0] = i
        for j in range(len_s2 + 1):
            dp[0][j] = j
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1])) + 1
        return dp[len_s1][len_s2]
