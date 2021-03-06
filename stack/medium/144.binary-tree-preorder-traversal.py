#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (49.10%)
# Total Accepted:    277.8K
# Total Submissions: 565.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
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
# Output: [1,2,3]
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
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        t = []
        p = root
        while p != None or len(t) != 0:
            if p != None:
                ans.append(p.val)
                t.append(p)
                p = p.left
            else:
                p = t.pop()
                p = p.right
        return ans
