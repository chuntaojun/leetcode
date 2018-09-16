class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)
        print nums
        for i in range(0, len(nums)):
            if i != nums[i]:
                return i
        return nums[len(nums) - 1] + 1


# Bit Manipulation
def BitFun(nums):
    for i in range(len(nums)):
        if i ^ nums[i] != 0:
            return i


# 二分查找法
def TwoPointsToFind(nums):
    pass


# 查找一个列表中所有缺失的数据
def myAns(nums):
    ans = []
    if nums[0] != 0:
        for i in range(nums[0]):
            ans.append(i)
    for j in range(len(nums) - 1):
        if nums[j + 1] - nums[j] != 1:
            for k in range(nums[j] + 1, nums[j + 1]):
                ans.append(k)
    if len(ans) == 0:
        return nums[len(nums) - 1] + 1
    return ans


s = Solution()
print s.missingNumber()
