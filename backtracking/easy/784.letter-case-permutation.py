#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (54.45%)
# Total Accepted:    33.2K
# Total Submissions: 60.9K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = set()
        self.calcAllPermutation(nums=list(S), start=0, end=len(S) - 1, ans=ans)
        return list(ans)
    
    def calcAllPermutation(self, nums, start, end, ans):
        if start > end:
            t = ''
            for i in range(end + 1):
                t += nums[i]
            ans.add(t)
            return
        tmp = nums[start]
        if (nums[start] >= 'a' and nums[start] <= 'z') or (nums[start] >= 'A' and nums[start] <= 'Z'):
            nums[start] = nums[start].upper()
            self.calcAllPermutation(nums=nums, start=start + 1, end=end, ans=ans)
            nums[start] = nums[start].lower()
            self.calcAllPermutation(nums=nums, start=start + 1, end=end, ans=ans)
            nums[start] = tmp
        else:
            t = ''
            for i in range(end + 1):
                t += nums[i]
            ans.add(t)
            self.calcAllPermutation(nums=nums, start=start + 1, end=end, ans=ans)

if __name__ == '__main__':
    s = Solution()
    t = ""
    print(s.letterCasePermutation(S=t))
