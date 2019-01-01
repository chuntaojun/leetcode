#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (36.55%)
# Total Accepted:    213.9K
# Total Submissions: 585.3K
# Testcase Example:  '{}'
#
# Given a binary tree
# 
# 
# struct TreeLinkNode {
# ⁠ TreeLinkNode *left;
# ⁠ TreeLinkNode *right;
# ⁠ TreeLinkNode *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the
# same level, and every parent has two children).
# 
# 
# Example:
# 
# Given the following perfect binary tree,
# 
# 
# ⁠    1
# ⁠  /  \
# ⁠ 2    3
# ⁠/ \  / \
# 4  5  6  7
# 
# 
# After calling your function, the tree should look like:
# 
# 
# ⁠    1 -> NULL
# ⁠  /  \
# ⁠ 2 -> 3 -> NULL
# ⁠/ \  / \
# 4->5->6->7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        if root.left != None:
            root.left.next = root.right
            if root.next != None:
                root.right.left = root.next.left
        self.connect(root=root.left)
        self.connect(root=root.right)
    
    def bfsConnect(self, root):
        if root == None:
            return
        tmp = []
        _stack = []
        _stack.append(root)
        size = len(_stack)
        while len(_stack) !=0:
            while size == 0:
                tmp.append(None)
                for i in range(len(tmp) - 1):
                    tmp[i].next = tmp[i + 1]
                tmp = []
                size = len(_stack)
            node = _stack.pop(0)
            tmp.append(node)
            size -= 1
            if node.left != None:
                _stack.append(node.left)
            if node.right != None:
                _stack.append(node.right)
        tmp.append(None)
        for i in range(len(tmp) - 1):
            tmp[i].next = tmp[i + 1]
