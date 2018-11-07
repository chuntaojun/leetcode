#
# [494] Target Sum
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (36.30%)
# Total Accepted:    1.2K
# Total Submissions: 3.3K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或
# -中选择一个符号添加在前面。
# 
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
# 
# 示例 1:
# 
# 
# 输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
# 
# 
# 注意:
# 
# 
# 数组的长度不会超过20，并且数组中的值全为正数。
# 初始的数组的和不会超过1000。
# 保证返回的最终结果为32位整数。
# 
# 
# 解题要点：能够找到一个序列，使得这个序列的和为 nums的和加上目标数s的和的总和的一半
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = 0
        for i in nums:
            sums += abs(i)
        len_n = len(nums)
        target = int((sums + S) / 2)
        if target != (sums + S) / 2 or sums < target or len_n == 0:
            return 0
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in nums:
            for j in range(target, i - 1, -1):
                dp[j] += dp[j - i]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
