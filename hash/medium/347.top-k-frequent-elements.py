#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (52.23%)
# Total Accepted:    158.1K
# Total Submissions: 302.7K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        topK = {}
        for i in range(len(nums)):
            if topK.__contains__(nums[i]):
                topK[nums[i]] += 1
            else:
                topK[nums[i]] = 0
        arr = []
        for t, v in topK.items():
            arr.append((t, v))
        self.quickSort(arr=arr, start=0, end=len(arr) - 1)
        return [arr[i][0] for i in range(k)]
    
    def quickSort(self, arr, start, end):
        if start < end:
            i = start
            j = end
            key = arr[int((start+end)/2)][1]
            while i <= j:
                while arr[i][1] > key:
                    i += 1
                while arr[j][1] < key:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i+=1
                    j-=1
            self.quickSort(arr, start, j)
            self.quickSort(arr, i, end)

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums=nums, k=k))
