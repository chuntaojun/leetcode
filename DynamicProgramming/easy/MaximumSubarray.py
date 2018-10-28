"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp = [nums[i] for i in range(len(nums))]
        max_sum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i - 1], dp[i])
            max_sum = max(dp[i], max_sum)
        return max_sum


if __name__ == '__main__':
    s = Solution()
    test = [-2, 1]
    print(s.maxSubArray(test))
