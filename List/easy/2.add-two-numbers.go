package easy

type ListNode struct {
	Val int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	ans := &ListNode{Val: 0, Next: nil}
	tNode := ans
	for l1 != nil && l2 != nil {
		a := l1.Val
		b := l2.Val
		tSum := a + b
		single := tSum % 10
		tNode.Next = &ListNode{Val: single, Next: nil}
		tNode = tNode.Next
		if l1.Next == nil && l2.Next == nil {
			tNode = &ListNode{Val: tSum / 10, Next: nil}
		} else if l1.Next == nil && l2.Next != nil {
			l2 = l2.Next
			l2.Val += tSum / 10
		} else if l1.Next != nil && l2.Next == nil {
			l1 = l1.Next
			l1.Val += tSum / 10
		} else {
			l1 = l1.Next
			l2 = l2.Next
			l2.Val += tSum / 10
		}
	}
	tmp := 0
	for l1 != nil {
		tmp = (tmp + l1.Val) / 10
		tNode.Next = &ListNode{Val: (tmp + l1.Val) % 10, Next: nil}
		l1 = l1.Next
		tNode = tNode.Next
	}
	for l2 != nil {
		tmp = (tmp + l2.Val) / 10
		tNode.Next = &ListNode{Val: (tmp + l2.Val) % 10, Next: nil}
		l2 = l2.Next
		tNode = tNode.Next
	}
	return ans
}