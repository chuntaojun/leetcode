#
# [983] Validate Stack Sequences
#
# https://leetcode.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (55.89%)
# Total Accepted:    4.4K
# Total Submissions: 7.8K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# Given two sequences pushed and popped with distinct values, return true if
# and only if this could have been the result of a sequence of push and pop
# operations on an initially empty stack.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# 
# 
# 
# Example 2:
# 
# 
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
# 
# 
# 
#
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        tmp = []
        i = 0
        while len(popped) > 0 and i < len(pushed):
            if pushed[i] == popped[0]:
                popped.remove(popped[0])
                i += 1
                continue
            elif len(tmp) > 0 and tmp[0] == popped[0]:
                tmp.remove(tmp[0])
                popped.remove(popped[0])
            else:
                tmp.insert(0, pushed[i])
                i += 1
        return tmp == popped


if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5]
    b = [4,5,3,2,1]
    print(s.validateStackSequences(pushed=a, popped=b))
