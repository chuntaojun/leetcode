#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Easy (32.22%)
# Total Accepted:    7.1K
# Total Submissions: 21.9K
# Testcase Example:  '1\n2'
#
# Given two integers A and B, return any string S such that:
# 
# 
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b'
# letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = 4, B = 1
# Output: "aabaa"
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.
# 
#
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        diff = abs(A - B)
        if diff < 2:
            s = ''
            while A != 0 and B != 0:
                A -= 1
                s += 'a'
                B -= 1
                s += 'b'
            while A != 0:
                A -= 1
                s += 'a'
            while B != 0:
                B -= 1
                s += 'b'
            return s
        else:
            if A > B:
                t = 1
                s = ''
                while A != 0 and B != 0:
                    A -= 1
                    s += 'a'
                    if diff > 0:
                        diff -= t
                        for _ in range(t):
                            s += 'a'
                            A -= 1
                    B -= 1
                    s += 'b'
                while A != 0:
                    A -= 1
                    s += 'a'
                while B != 0:
                    B -= 1
                    s += 'b'
                return s
            else:
                t = 1
                s = ''
                while A != 0 and B != 0:
                    B -= 1
                    s += 'b'
                    if diff > 0:
                        diff -= t
                        for _ in range(t):
                            s += 'b'
                            B -= 1
                    A -= 1
                    s += 'a'
                while A != 0:
                    A -= 1
                    s += 'a'
                while B != 0:
                    B -= 1
                    s += 'b'
                return s


if __name__ == '__main__':
    s = Solution()
    A = 12
    B = 13
    print(s.strWithout3a3b(A=A, B=B))
