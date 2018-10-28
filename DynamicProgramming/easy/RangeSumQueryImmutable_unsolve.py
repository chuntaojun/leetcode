"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        dp = [nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i]
        self.dp = dp

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    s = NumArray(nums)
    print(s.dp)
    print(s.sumRange(0, 2))
    print(s.sumRange(2, 5))
    print(s.sumRange(0, 5))
