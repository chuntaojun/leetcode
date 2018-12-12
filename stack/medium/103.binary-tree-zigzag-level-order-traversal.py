#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (39.26%)
# Total Accepted:    177K
# Total Submissions: 450.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        ans = []
        tmp = []
        q.append(root)
        if root is None:
            return []
        now_node_size = len(q)
        while (len(q) != 0):
            if now_node_size == 0:
                ans.append(tmp)
                tmp = []
                now_node_size = len(q)
            node = q[0]
            q.remove(node)
            now_node_size -= 1
            tmp.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        ans.append(tmp)

        def change(a):
            a.reverse()
            return a

        return [ans[i] if i % 2 == 0 else change(a=ans[i]) for i in range(len(ans)) ]
