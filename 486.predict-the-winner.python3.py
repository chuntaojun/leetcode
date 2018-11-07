#
# [486] Predict the Winner
#
# https://leetcode-cn.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (40.24%)
# Total Accepted:    579
# Total Submissions: 1.4K
# Testcase Example:  '[1,5,2]'
#
# 给定一个表示分数的非负整数数组。
# 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
# 
# 给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。
# 
# 示例 1:
# 
# 
# 输入: [1, 5, 2]
# 输出: False
# 解释: 一开始，玩家1可以从1和2中进行选择。
# 如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
# 所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
# 因此，玩家1永远不会成为赢家，返回 False。
# 
# 
# 示例 2:
# 
# 
# 输入: [1, 5, 233, 7]
# 输出: True
# 解释: 玩家1一开始选择1。然后玩家2必须从5和7中进行选择。无论玩家2选择了哪个，玩家1都可以选择233。
# 最终，玩家1（234分）比玩家2（12分）获得更多的分数，所以返回 True，表示玩家1可以成为赢家。
# 
# 
# 注意:
# 
# 
# 1 <= 给定的数组长度 <= 20.
# 数组里所有分数都为非负数且不会大于10000000。
# 如果最终两个玩家的分数相等，那么玩家1仍为赢家。
# 
# 
#
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_n = len(nums)
        dp = [[0 for j in range(len_n)] for i in range(len_n)]
        prefixSum = [0 for i in range(len_n + 1)]
        for i in range(0, len_n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        for i in range(1, len_n + 1):
            for lhs in range(len_n + 1 - i):
                rhs = lhs + i - 1
                if lhs == rhs:
                    dp[lhs][rhs] = nums[lhs]
                elif lhs == rhs - 1:
                    dp[lhs][rhs] = max(nums[lhs], nums[rhs])
                else:
                    # 选取左边的数字后玩家一目前的积分
                    pickLeft = nums[lhs] + prefixSum[rhs + 1] - prefixSum[lhs + 1] - dp[lhs + 1][rhs]
                    # 选取右边的数字后玩家一目前的积分
                    pickRight = nums[rhs] + prefixSum[rhs] - prefixSum[lhs] - dp[lhs][rhs - 1]
                    dp[lhs][rhs] = max(pickLeft, pickRight)
        return dp[0][len_n - 1] >= (int(prefixSum[-1] / 2) + prefixSum[-1] % 2)


if __name__ == '__main__':
    s = Solution()
    print(s.PredictTheWinner([1,5,233,7]))
