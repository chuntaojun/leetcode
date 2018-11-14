#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (56.39%)
# Total Accepted:    51.8K
# Total Submissions: 91.8K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# Output: [1, 3, 9]
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        ans = []
        tmp = -sys.maxsize - 1
        q.append(root)
        if root is None:
            return []
        now_node_size = len(q)
        while (len(q) != 0):
            if now_node_size == 0:
                ans.append(tmp)
                tmp = -sys.maxsize - 1
                now_node_size = len(q)
            node = q[0]
            q.remove(node)
            now_node_size -= 1
            tmp = max(tmp, node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        ans.append(tmp)
        return ans


