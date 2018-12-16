#
# @lc app=leetcode id=671 lang=python
#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (42.77%)
# Total Accepted:    37.7K
# Total Submissions: 88.2K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. 
# 
# 
# 
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree. 
# 
# 
# 
# If no such second minimum value exists, output -1 instead.
# 
# 
# Example 1:
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# 
# 
# Example 2:
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -1
        self._stack = []
        self.pre_order(root=root)
        self._stack.sort()
        if self._stack[0] == self._stack[-1]:
            return -1
        else:
            for i in range(1, len(self._stack)):
                if self._stack[i] > self._stack[0]:
                    return self._stack[i]
            return -1
    
    def pre_order(self, root):
        if root != None:
            self._stack.append(root.val)
            self.pre_order(root=root.left)
            self.pre_order(root=root.right)