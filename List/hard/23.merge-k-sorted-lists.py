#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (31.62%)
# Total Accepted:    306.2K
# Total Submissions: 968.6K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.

# 仅适用于python2
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        h = []
        head = ListNode(-1)
        tmp = head
        while len(lists) != 0:
            i = 0
            while i < len(lists):
                if lists[i] == None:
                    lists.pop(i)
                else:
                    heapq.heappush(h, (lists[i].val, lists[i]))
                    lists[i] = lists[i].next
                    i += 1
            if len(h) != 0:
                _, node = heapq.heappop(h)
                node.next = None
                tmp.next = node
                tmp = tmp.next
        while len(h) > 0:
            _, node = heapq.heappop(h)
            node.next = None
            tmp.next = node
            tmp = tmp.next
        return head.next
