#
# @lc app=leetcode id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (64.28%)
# Total Accepted:    19.8K
# Total Submissions: 30.8K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the preorder traversal of its nodes' values.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# Return its preorder traversal as: [1,3,5,6,2,4].
# 
# 
# 
# Note:
# 
# Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.ans = []
        self.pre_order(root=root)
        return self.ans

    def pre_order(self, root):
        if root != None:
            tmp_child = root.children
            for i in range(len(tmp_child)):
                self.pre_order(root=tmp_child[i])
                self.ans.append(root.val)
        return
