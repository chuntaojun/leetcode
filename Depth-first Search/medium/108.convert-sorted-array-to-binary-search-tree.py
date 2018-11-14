#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (47.33%)
# Total Accepted:    211.8K
# Total Submissions: 447.5K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        tmp = []
        right = 0
        tmpNode = head
        while tmpNode is not None:
            tmpNode = tmpNode.next
            right += 1
        tmp.append(head)
        return self.build(li=tmp, left=0, right=right - 1)
    
    def build(self, li, left, right):
        if left > right:
            return None
        m = int((left + right) / 2)
        lNode = self.build(li=li, left=left, right=m - 1)
        root = TreeNode(x=li[0].val)
        root.left = lNode
        li[0] = li[0].next
        root.right = self.build(li=li, left=m + 1, right=right)
        return root

