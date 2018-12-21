#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (44.36%)
# Total Accepted:    290.1K
# Total Submissions: 653.8K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.qSort(arr=nums, left=0, right=len(nums) - 1)
        return nums[-1 * k]
    
    def qSort(self, arr, left, right):
        if left < right:
            q = self.partition(arr=arr, left=left, right=right)
            self.qSort(arr=arr, left=left, right=q - 1)
            self.qSort(arr=arr, left=q + 1, right=right)
    
    def partition(self, arr, left, right):
        x = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= x:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(s.findKthLargest(nums=nums, k=k))
