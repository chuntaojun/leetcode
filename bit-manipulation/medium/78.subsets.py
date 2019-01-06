#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (49.67%)
# Total Accepted:    309.6K
# Total Submissions: 622.9K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        size = int(pow(2, len(nums)))
        hash_n = 1
        while hash_n <= size:
            t = []
            for i in range(len(nums)):
                a = 1 << i
                if a&hash_n:
                    t.append(nums[i])
            ans.append(t)
            hash_n += 1
        return ans
        
if __name__ == '__main__':
    s = Solution()
    t = [1,2,3]
    print(s.subsets(nums=t))
    
