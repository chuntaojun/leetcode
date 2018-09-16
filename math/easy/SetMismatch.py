class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        ans = []
        sums = len(nums) * (len(nums) + 1) / 2 - nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                ans.append(nums[i])
            sums -= nums[i]
        if sums < 0:
            ans.append(ans[0] + sums)
        elif sums > 0:
            ans.append(ans[0] + sums)
        return ans
