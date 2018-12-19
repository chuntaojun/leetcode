#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (33.99%)
# Total Accepted:    237.1K
# Total Submissions: 697.6K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# 
# 
# pop() -- Removes the element on top of the stack.
# 
# 
# top() -- Get the top element.
# 
# 
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_num = []
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.q.append(x)
        if len(self.min_num) == 0:
            self.min_num.append(x) 
        elif x > self.min_num[-1]:
            x = self.min_num[-1]
        self.min_num.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.min_num.pop()
        return self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_num[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
