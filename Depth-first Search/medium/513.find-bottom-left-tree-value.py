#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (57.08%)
# Total Accepted:    58K
# Total Submissions: 101.7K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, find the leftmost value in the last row of the tree. 
# 
# 
# Example 1:
# 
# Input:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Output:
# 1
# 
# 
# 
# ⁠ Example 2: 
# 
# Input:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# Output:
# 7
# 
# 
# 
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
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
        return ans[0][0]

    