/*
 * @lc app=leetcode id=19 lang=golang
 *
 * [19] Remove Nth Node From End of List
 *
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 *
 * algorithms
 * Medium (33.67%)
 * Total Accepted:    321.4K
 * Total Submissions: 954.8K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given a linked list, remove the n-th node from the end of list and return
 * its head.
 * 
 * Example:
 * 
 * 
 * Given linked list: 1->2->3->4->5, and n = 2.
 * 
 * After removing the second node from the end, the linked list becomes
 * 1->2->3->5.
 * 
 * 
 * Note:
 * 
 * Given n will always be valid.
 * 
 * Follow up:
 * 
 * Could you do this in one pass?
 * 
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

package medium

type ListNode struct {
	Val int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	length := 0
	if head == nil {
		return head
	}
	tmp := head
	for tmp != nil {
		length += 1
		tmp = tmp.Next
	}
    if length == n {
        return head.Next
    }
	length = length - n - 1
	tmp = head
	for length > 0 {
		tmp = tmp.Next
        length -= 1
	}
	if tmp.Next != nil {
		tmp.Next = tmp.Next.Next
	}
	return head
}
