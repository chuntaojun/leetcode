#
# @lc app=leetcode id=783 lang=python
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (49.12%)
# Total Accepted:    22.2K
# Total Submissions: 45.2K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
# 
# Example :
# 
# 
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
# 
# 
# Note:
# 
# 
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
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
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = []
        self.preOrder(root=root)
        self.minNum = self.ans[-1]
        a = 0; b = 1
        while b < len(self.ans):
            self.minNum = min(self.minNum, abs(self.ans[b] - self.ans[a]))
            a += 1
            b += 1
        return self.minNum
    
    def preOrder(self, root):
        if root != None:
            self.preOrder(root=root.left)
            self.ans.append(root.val)
            self.preOrder(root=root.right)



        
class Heap(object):
    def __init__(self):
        self.size = 0
        self.cap = 100
        self.elements = [-1 * sys.maxsize for i in range(101)]
    
    def insert(self, val):
        self.size += 1
        i = self.size
        while self.elements[int(i / 2)] > val:
            self.elements[i] = self.elements[int(i / 2)]
            i = int(i / 2)
        self.elements[i] = val
    
    def deleteMin(self):
        minElement = self.elements[1]
        lastElement = self.elements[self.size]
        self.size -= 1
        i = 1
        while 2 * i <= self.size:
            child = i * 2
            if child != self.size and self.elements[child] > self.elements[child + 1]:
                child += 1
            if lastElement > self.elements[child]:
                self.elements[i] = self.elements[child]
            i = child
        self.elements[i] = lastElement
        return minElement
