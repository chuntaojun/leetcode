#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (32.87%)
# Total Accepted:    45.2K
# Total Submissions: 137.5K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# Note: The length of path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input:
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree
# is not more than 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.maxL = 0
        self.getMax(root=root, val=root.val)
        return self.maxL
    
    def getMax(self, root, val):
        if root == None:
            return 0
        leftH = self.getMax(root=root.left, val=root.val)
        rightH = self.getMax(root=root.right, val=root.val)
        self.maxL = max(self.maxL, leftH + rightH)
        if root.val == val:
            return max(leftH, rightH) + 1
        return 0
