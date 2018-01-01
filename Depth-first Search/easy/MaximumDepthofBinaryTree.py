"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height_1 = self.maxDepth(root.left)
        height_2 = self.maxDepth(root.right)
        return height_1 + 1 if height_1 > height_2 else height_2 + 1


if __name__ == '__main__':
    pass
