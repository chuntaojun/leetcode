#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (48.66%)
# Total Accepted:    316.5K
# Total Submissions: 650.5K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.dfs(p=p, q=q)
    
    def dfs(self, p, q):
        if p is None and q is None:
            return True
        if not (self.leftIsNone(p, q) and self.rightIsNone(p, q)):
            return False
        return self.isEqNodeVal(p, q) and self.dfs(p=p.left, q=q.left) and self.dfs(p=p.right, q=q.right)
        
    def leftIsNone(self, p, q):
        return p.left is None and q.left is None
    
    def rightIsNone(self, p, q):
        return p.right is None and q.right is None
    
    def isEqNodeVal(self, p, q):
        return p.val == q.val
