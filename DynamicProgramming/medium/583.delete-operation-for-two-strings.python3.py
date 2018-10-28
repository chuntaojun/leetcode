#
# [583] Delete Operation for Two Strings
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (36.52%)
# Total Accepted:    436
# Total Submissions: 1.2K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 
# 示例 1:
# 
# 
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
# 
# 
# 说明:
# 
# 
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。
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
        len_n1 = len(word1)
        len_n2 = len(word2)
        dp = [[0 for i in range(len_n2 + 1)] for j in range(len_n1 + 1)]
        for i in range(1, len_n1 + 1):
            for j in range(1, len_n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len_n1 + len_n2 - 2 * dp[len_n1][len_n2]
