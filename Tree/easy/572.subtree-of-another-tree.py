#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (40.70%)
# Total Accepted:    76.4K
# Total Submissions: 187.8K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.ans = False
        if t == None or s == None:
            return False
        self.findTarget(root=s, t=t)
        return self.ans
    
    def findTarget(self, root, t):
        if root != None:
            if root.val == t.val:
                if self.compare(s=root, t=t):
                    self.ans = True
            self.findTarget(root=root.left, t=t)
            self.findTarget(root=root.right, t=t)

    def compare(self, s, t):
        if s != None and t != None:
            if s.val == t.val:
                return self.compare(s=s.left, t=t.left) and self.compare(s=s.right, t=t.right)
            else:
                return False
        if (s == None and t != None) or (s != None and t == None):
            return False
        return True
        