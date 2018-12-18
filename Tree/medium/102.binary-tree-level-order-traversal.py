#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (45.84%)
# Total Accepted:    307.5K
# Total Submissions: 670.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ans = []
        tmp = []
        _stack = []
        _stack.append(root)
        now_node_size = len(_stack)
        while len(_stack) != 0:
            if now_node_size == 0:
                ans.append(tmp)
                tmp = []
                now_node_size = len(_stack)
            p = _stack.pop(0)
            now_node_size -= 1
            tmp.append(p.val)
            if p.left != None:
                _stack.append(p.left)
            if p.right != None:
                _stack.append(p.right)
        ans.append(tmp)
        return ans
