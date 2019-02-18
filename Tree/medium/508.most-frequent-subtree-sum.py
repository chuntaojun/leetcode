#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (53.69%)
# Total Accepted:    43.9K
# Total Submissions: 81.8K
# Testcase Example:  '[5,2,-3]'
#
# 
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
# 
# 
# Examples 1
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
# 
# 
# Examples 2
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# return [2], since 2 happens twice, however -5 only occur once.
# 
# 
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        arr = defaultdict(int)
        self.func(node=root, arr=arr)
        arr = sorted(arr.items(), key=lambda item: item[1], reverse=True)
        maxL = arr[0][1]
        result = []
        for i in range(len(arr)):
            if arr[i][1] < maxL:
                break
            result.append(arr[i][0])
        return result
    
    def func(self, node, arr):
        if node and (node.left or node.right):
            l = self.func(node=node.left, arr=arr)
            r = self.func(node=node.right, arr=arr)
            arr[l + r + node.val] += 1
            return l + r + node.val
        if node:
            arr[node.val] += 1
            return node.val
        return 0




if __name__ == '__main__':
    s = Solution()
