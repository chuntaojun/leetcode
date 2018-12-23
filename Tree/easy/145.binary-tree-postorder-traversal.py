#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (45.70%)
# Total Accepted:    220.6K
# Total Submissions: 482.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if  root == None:
            return []
        p = root
        self.t = []
        self.ans = []
        while len(self.t) != 0 or p != None:
            while p != None:
                self.t.append(p)
                p = p.right
            if len(self.t) != 0:
                p = self.t.pop()
                self.ans.append(p.val)
                p = p.left
        self.ans.reverse()
        return self.ans
