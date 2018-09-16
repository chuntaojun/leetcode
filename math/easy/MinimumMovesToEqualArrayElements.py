class Solution(object):
    def minMoves(self, nums):
        nums.sort()
        times = 0
        for i in range(1, len(nums)):
            times += nums[i] - nums[0]
        return times
