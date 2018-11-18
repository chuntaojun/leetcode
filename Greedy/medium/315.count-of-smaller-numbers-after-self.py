#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (36.02%)
# Total Accepted:    60.9K
# Total Submissions: 169.1K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
#
# 常规解法，时间复杂度 O(N^2)
# class Solution(object):
#     def countSmaller(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         for i in range(len(nums)):
#             count = 0
#             for j in range(i + 1, len(nums)):
#                 if nums[j] < nums[i]:
#                     count += 1
#             ans.append(count)
#         return ans
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = []
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            left = 0; right = len(tmp)
            while left < right:
                mid = left + int((right - left) / 2)
                if tmp[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1
            ans.append(left)
            tmp.insert(left, nums[i])
        ans.reverse()
        return ans
