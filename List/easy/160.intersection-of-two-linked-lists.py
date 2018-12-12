#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (30.86%)
# Total Accepted:    247.8K
# Total Submissions: 803K
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists: 
# 
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗            
# B:     b1 → b2 → b3
# 
# begin to intersect at node c1.
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns. 
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
# 
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        if headA == None or headB == None:
            return
        while pA and pB:
            if pA.val != pB.val:
                if pA.next and pB.next:
                    pA = pA.next
                    pB = pB.next
                elif pA.next == None and pB.next != None:
                    pA = headB
                    pB = pB.next
                elif pB.next == None and pA.next != None:
                    pA = pA.next
                    pB = headA
                else:
                    return
            else:
                return pA
