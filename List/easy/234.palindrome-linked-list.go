/*
 * @lc app=leetcode id=234 lang=golang
 *
 * [234] Palindrome Linked List
 *
 * https://leetcode.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (34.82%)
 * Total Accepted:    215K
 * Total Submissions: 617.3K
 * Testcase Example:  '[1,2]'
 *
 * Given a singly linked list, determine if it is a palindrome.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2
 * Output: false
 * 
 * Example 2:
 * 
 * 
 * Input: 1->2->2->1
 * Output: true
 * 
 * Follow up:
 * Could you do it in O(n) time and O(1) space?
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
	Val int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
    if head == nil {
        return true
    }
	slow := head
	fast := head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	slow.Next = reverseList(slow.Next)
	f1 := head
	f2 := slow.Next
	for f1 != nil && f2 != nil {
		if f1.Val != f2.Val {
			return false
		}
		f1 = f1.Next
		f2 = f2.Next
	}
	return true
}

func reverseList(head *ListNode) *ListNode {
	newHead := head
	p := head
	for p != nil && p.Next != nil {
		t := newHead
		newHead = p.Next
		p.Next = newHead.Next
		newHead.Next = t
	}
	return newHead
}
