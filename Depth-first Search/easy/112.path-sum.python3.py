#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (36.13%)
# Total Accepted:    257K
# Total Submissions: 711.3K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.ans = []
        self.dfs(node=root, l=[0])
        for i in range(len(self.ans)):
            if self.ans[i] == sum:
                return True
        return False
    
    def dfs(self, node, l):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.ans.append(l.pop() + node.val)
            return
        l.append(l.pop() + node.val)
        self.dfs(node=node.left, l=l.copy())
        self.dfs(node=node.right, l=l.copy())
