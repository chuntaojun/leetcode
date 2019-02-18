/*
 * @lc app=leetcode id=889 lang=golang
 *
 * [889] Construct Binary Tree from Preorder and Postorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (57.56%)
 * Total Accepted:    11K
 * Total Submissions: 19.2K
 * Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
 *
 * Return any binary tree that matches the given preorder and postorder
 * traversals.
 * 
 * Values in the traversals pre and post are distinct positive integers.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
 * Output: [1,2,3,4,5,6,7]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= pre.length == post.length <= 30
 * pre[] and post[] are both permutations of 1, 2, ..., pre.length.
 * It is guaranteed an answer exists. If there exists multiple answers, you can
 * return any of them.
 * 
 * 
 * 
 */
package medium

type TreeNode struct {
	Val int
	Left *TreeNode
 	Right *TreeNode
}

func constructFromPrePost(pre []int, post []int) *TreeNode {
	return buildTree(pre, post, 0, 0, len(post) - 1)
}

func buildTree(pre, post []int, loc, postL, postR int) *TreeNode {
	if loc >= len(pre) || postL > postR {
		return nil
	}
	root := &TreeNode{Val: pre[loc]}
	for i := postL; i < postR; i ++ {
		if post[i] == pre[loc + 1] {
			root.Left = buildTree(pre, post, loc + 1, postL, i)
			root.Right = buildTree(pre, post, loc + i + 2 - postL, i + 1, postR - 1)
		}
	}
	return root
}
