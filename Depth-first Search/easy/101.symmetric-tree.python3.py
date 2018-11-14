#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (41.72%)
# Total Accepted:    313.4K
# Total Submissions: 751.3K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :doc 将root分为左右子树同时先序遍历
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            return False
        list_1 = []
        list_2 = []
        self.pre(tree=root.left, l=list_1)
        self.pre_2(tree=root.right, l=list_2)
        print(list_1)
        print(list_2)
        if len(list_1) == len(list_2):
            for i in range(len(list_1)):
                if list_1[i] != list_2[i]:
                    return False
            return True
        return False
    
    def pre(self, tree, l):
        """

        :param tree: TreeNode
        :param l: list
        :return:
        """
        if tree is not None:
            l.append(tree.val)
            self.pre(tree.left, l)
            self.pre(tree.right, l)
        if tree is None:
            l.append(None)
    
    def pre_2(self, tree, l):
        if tree is not None:
            l.append(tree.val)
            self.pre_2(tree.right, l)
            self.pre_2(tree.left, l)
        if tree is None:
            l.append(None)