"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

import operator


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        list_1, list_2 = [], []
        self.pre(p, list_1)
        self.pre(q, list_2)
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
