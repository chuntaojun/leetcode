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
        return 0 == cmp(list_1, list_2)

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


if __name__ == '__main__':
    pass
