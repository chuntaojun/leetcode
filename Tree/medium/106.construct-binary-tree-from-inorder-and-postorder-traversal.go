/*
 * @lc app=leetcode id=106 lang=golang
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (37.11%)
 * Total Accepted:    134.4K
 * Total Submissions: 361.7K
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * Given inorder and postorder traversal of a tree, construct the binary tree.
 * 
 * Note:
 * You may assume that duplicates do not exist in the tree.
 * 
 * For example, given
 * 
 * 
 * inorder = [9,3,15,20,7]
 * postorder = [9,15,7,20,3]
 * 
 * Return the following binary tree:
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package medium

type TreeNode struct {
	Val	int
	Left	*TreeNode
	Right	*TreeNode
}

func buildTree(inorder []int, postorder []int) *TreeNode {
    return constructTree(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
}

func constructTree(inorder []int, postorder []int, il, ir, pl, pr int) *TreeNode {
	if il > ir || pl > pr {
		return nil
	}
	root := &TreeNode{Val: postorder[pr]}
	for i := il; i <= ir; i ++ {
		if inorder[i] == postorder[pr] {
			root.Left = constructTree(inorder, postorder, il, i - 1, pl, pl + i - il - 1)
			root.Right = constructTree(inorder, postorder, i + 1, ir, pl + i - il, pr - 1)
		}
	}
	return root
}
