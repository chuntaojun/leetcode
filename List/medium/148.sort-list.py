#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (32.66%)
# Total Accepted:    158.3K
# Total Submissions: 484.6K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return None if head == None else self.mergeSort(node=head)
    
    def mergeSort(self, node):
        if node.next == None:
            return node
        p = node; q = node; pre = None
        while q != None and q.next != None:
            pre = p
            p = p.next
            q = q.next.next
        pre.next = None
        l = self.mergeSort(node)
        r = self.mergeSort(p)
        return self.merge(l1=l, l2=r)
    
    def merge(self, l1, l2):
        node = ListNode(-1)
        tmp = node
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
            else:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
        while l1 != None:
            tmp.next = l1
            l1 = l1.next
            tmp = tmp.next
        while l2 != None:
            tmp.next = l2
            l2 = l2.next
            tmp = tmp.next
        tmp = None
        return node.next
