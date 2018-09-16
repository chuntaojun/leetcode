"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums[0], nums[len(nums) - 1])
        dp = [i for i in nums]
        for i in range(0, len(nums)):
            for j in range(i + 2, len(nums)):
                dp[j] = max(nums[j] + dp[i], dp[j])
        dp.sort()
        return dp[len(dp) - 1]


if __name__ == '__main__':
    s = Solution()
    test = [1,3,1]
    print s.rob(test)
