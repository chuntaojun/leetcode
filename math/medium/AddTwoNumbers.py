class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1, l2 = JudgeWhoIsLong(l1, l2)
        new_node = ListNode(0)
        while l1 is not None:
            while l2 is not None:
                temp = l1.val + l2.val
                l1.val = temp % 10
                l1.next.val = temp / 10
                l1 = l1.next
                l2 = l2.next
            if l1.val > 9 and l1.next is not None:
                l1.val = l1.val % 10
                l1.next.val += 1
            elif l1.val > 9 and l1.next is None:
                new_node.val = 1
                l1.val -= 10
                l1.next = new_node
            l1 = l1.next
        if new_node.val == 0:
            return l1
        return new_node


def JudgeWhoIsLong(l1, l2):
    temp_l1, temp_l2 = l1, l2
    while True:
        temp_l1 = temp_l1.next
        temp_l2 = temp_l2.next
        if temp_l1 is None:
            return l2, l1
        if temp_l2 is None:
            return l1, l2
