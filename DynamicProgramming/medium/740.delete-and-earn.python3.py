#
# [740] Delete and Earn
#
# https://leetcode-cn.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (44.00%)
# Total Accepted:    466
# Total Submissions: 1.1K
# Testcase Example:  '[3,4,2]'
#
# 给定一个整数数组 nums ，你可以对它进行一些操作。
# 
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] +
# 1 的元素。
# 
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
# 
# 示例 1:
# 
# 
# 输入: nums = [3, 4, 2]
# 输出: 6
# 解释: 
# 删除 4 来获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [2, 2, 3, 3, 3, 4]
# 输出: 9
# 解释: 
# 删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
# 
# 
# 注意:
# 
# 
# nums的长度最大为20000。
# 每个整数nums[i]的大小都在[1, 10000]范围内。
# 
# 
# 深度搜索版本（超时）
class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for i in range(len(nums)):
            tmp = max(tmp, nums[i] + self.dfs(nums, nums[i]))
        return tmp
    
    def dfs(self, nums, target):
        tmp = []
        times = 0
        # 选中点数后更新nums列表
        for i in range(len(nums)):
            if nums[i] == target + 1 or nums[i] == target - 1:
                continue
            if nums[i] == target and times == 0:
                times += 1
                continue
            tmp.append(nums[i])
        tmp_ans = 0
        for i in range(len(tmp)):
            tmp_ans = max(tmp_ans, tmp[i] + self.dfs(tmp, tmp[i]))
        return tmp_ans


if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
