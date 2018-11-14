#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (44.27%)
# Total Accepted:    191.2K
# Total Submissions: 431.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
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
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root):
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
        ans.reverse()
        return ans
