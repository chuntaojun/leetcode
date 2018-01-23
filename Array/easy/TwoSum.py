"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """
        tmp_nums = [i for i in nums]
        tmp_nums.sort()
        max_loc = len(nums) - 1
        for i in range(len(tmp_nums)):
            if tmp_nums[i] >= target:
                max_loc = i
                break
        l, r = 0, max_loc
        while l > r:
            ans = tmp_nums[l] + tmp_nums[r]
            if ans == target:
                break
            elif ans > target:
                r -= 1
            else:
                l += 1
        l = nums.index(tmp_nums[l])
        nums[l] = -1
        r = nums.index(tmp_nums[r])
        return [nums.index(tmp_nums[l]), nums.index(tmp_nums[r])]


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([3, 3], 6)
