#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (52.14%)
# Total Accepted:    316.7K
# Total Submissions: 607.1K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.calcAllPermutation(nums=nums, start=0, end=len(nums) - 1, ans=ans)
        return ans
    
    def calcAllPermutation(self, nums, start, end, ans):
        if start == end:
            t = []
            for i in range(end + 1):
                t.append(nums[i])
            ans.append(t)
        else:
            for i in range(start, end + 1):
                nums[i], nums[start] = nums[start], nums[i]
                self.calcAllPermutation(nums=nums, start=start + 1, end=end, ans=ans)
                nums[i], nums[start] = nums[start], nums[i]


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    print(s.permute(nums=nums))
    