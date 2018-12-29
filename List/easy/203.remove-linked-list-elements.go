/*
 * @lc app=leetcode id=203 lang=golang
 *
 * [203] Remove Linked List Elements
 *
 * https://leetcode.com/problems/remove-linked-list-elements/description/
 *
 * algorithms
 * Easy (34.81%)
 * Total Accepted:    193.8K
 * Total Submissions: 556.9K
 * Testcase Example:  '[1,2,6,3,4,5,6]\n6'
 *
 * Remove all elements from a linked list of integers that have value val.
 * 
 * Example:
 * 
 * 
 * Input:  1->2->6->3->4->5->6, val = 6
 * Output: 1->2->3->4->5
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

package easy

type ListNode struct {
	Val	int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	a := &ListNode{}
	a.Next = head
	tmp := a
	for tmp != nil && tmp.Next != nil {
		l := tmp.Next
		if l.Val == val {
			tmp.Next = l.Next
		} else {
			tmp = tmp.Next
		}
	}
	return a.Next
}
