#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (36.46%)
# Total Accepted:    128.8K
# Total Submissions: 353.2K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(inorder=inorder, il=0, ir=len(inorder) - 1, postorder=postorder, pl=0, pr=len(postorder) - 1)
    
    def constructTree(self, inorder, il, ir, postorder, pl, pr):
        if il > ir or pl > pr:
            return None
        root = TreeNode(x=postorder[pr])
        for i in range(il, ir + 1):
            if inorder[i] == postorder[pr]:
                root.left = self.constructTree(inorder=inorder, il=il, ir =i - 1, postorder=postorder, pl=pl, pr=pl + i - il - 1)
                root.right = self.constructTree(inorder=inorder, il=i + 1, ir =ir, postorder=postorder, pl=pl + i - il, pr=pr - 1)
        return root
