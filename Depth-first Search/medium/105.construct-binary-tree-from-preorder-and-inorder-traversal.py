#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (37.59%)
# Total Accepted:    177.6K
# Total Submissions: 472.5K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
# Definition for a binary tree node.

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(preorder=preorder, pl=0, pr=len(preorder) - 1, inorder=inorder, il=0, ir=len(inorder) - 1)
    
    def constructTree(self, preorder, pl, pr, inorder, il, ir):
        if pl > pr or il > ir:
            return None
        root = TreeNode(x=preorder[pl])
        for k in range(il, ir + 1):
            if inorder[k] == preorder[pl]:
                root.left = self.constructTree(preorder=preorder, pl=pl + 1, pr=pl + k - il, inorder=inorder, il=il, ir=k - 1)
                root.right = self.constructTree(preorder=preorder, pl=pl + k - il + 1, pr=pr, inorder=inorder, il=k + 1, ir=ir)
        return root
        
