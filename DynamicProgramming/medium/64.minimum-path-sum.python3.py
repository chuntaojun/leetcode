#
# [64] Minimum Path Sum
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (55.30%)
# Total Accepted:    5.7K
# Total Submissions: 10.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_j = len(grid)
        len_i = len(grid[0])
        dp = [[-1 for j in range(len_i)] for i in range(len_j)]
        dp[0][0] = grid[0][0]
        for j in range(1, len_i):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, len_j):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, len_j):
            for j in range(1, len_i):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[len_j - 1][len_i - 1]
    