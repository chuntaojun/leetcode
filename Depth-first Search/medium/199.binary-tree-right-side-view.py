#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (45.06%)
# Total Accepted:    134.2K
# Total Submissions: 297.9K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def largestValues(self, root):
            """
        :type root: TreeNode
        :rtype: List[int]
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
                ans.append(tmp.pop())
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
        ans.append(tmp.pop())
        return ans
