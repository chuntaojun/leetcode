#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (45.59%)
# Total Accepted:    97.9K
# Total Submissions: 214.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 求左子树最大高度与右子树最大高度之和

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.ans = []
        self.ans.sort()
        return self.ans[-1]
    
    def Height(self, root):
        if root == None:
            return 0
        return 1 + max(self.Height(root.left), self.Height(root.right))
    
    def pre_order(self, root):
        if root != None:
            self.ans.append(self.Height(root=root.left) + self.Height(root=root.right))
            self.pre_order(root=root.left)
            self.pre_order(root=root.right)


class Solution2(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """