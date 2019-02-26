/*
 * @lc app=leetcode id=92 lang=golang
 *
 * [92] Reverse Linked List II
 *
 * https://leetcode.com/problems/reverse-linked-list-ii/description/
 *
 * algorithms
 * Medium (33.97%)
 * Total Accepted:    178.2K
 * Total Submissions: 524.4K
 * Testcase Example:  '[1,2,3,4,5]\n2\n4'
 *
 * Reverse a linked list from position m to n. Do it in one-pass.
 * 
 * Note: 1 ≤ m ≤ n ≤ length of list.
 * 
 * Example:
 * 
 * 
 * Input: 1->2->3->4->5->NULL, m = 2, n = 4
 * Output: 1->4->3->2->5->NULL
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 */
package medium

type ListNode struct {
    Val int
	Next *ListNode
}

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	tmp := head
    pre := head
	for i := 1; i < m; i ++ {
        pre = tmp
		tmp = tmp.Next
	}
	if m != 1 {
		pre.Next = reverse(tmp, n - m)
	} else {
		head = reverse(tmp, n - m)
	}
	return head
}

func reverse(node *ListNode, n int) *ListNode {
	newHead := node
	p := node
	for n > 0 && p != nil && p.Next != nil {
        n--
		t := newHead
		newHead = p.Next
		p.Next = newHead.Next
		newHead.Next = t
	}
	return newHead
}
