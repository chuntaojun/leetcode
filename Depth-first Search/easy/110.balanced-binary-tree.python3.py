#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (39.54%)
# Total Accepted:    266.9K
# Total Submissions: 675K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a, b = self.dfs(node=root)
        return a
    
    def dfs(self, node):
        if node is None:
            return True, 0
        blanced, leftHeigh = self.dfs(node=node.left)
        if not blanced:
            return False, 0
        blanced, rightHeigh = self.dfs(node=node.right)
        if not blanced:
            return False, 0
        return abs(leftHeigh - rightHeigh) <= 1, max(leftHeigh, rightHeigh) + 1
