#
# @lc app=leetcode id=838 lang=python
#
# [838] Push Dominoes
#
# https://leetcode.com/problems/push-dominoes/description/
#
# algorithms
# Medium (42.02%)
# Total Accepted:    8.2K
# Total Submissions: 19.5K
# Testcase Example:  '".L.R...LR..L.."'
#
# There are N dominoes in a line, and we place each domino vertically upright.
# 
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.
# 
# 
# 
# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left.
# 
# Similarly, the dominoes falling to the right push their adjacent dominoes
# standing on the right.
# 
# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.
# 
# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.
# 
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th
# domino has been pushed to the left; S[i] = 'R', if the i-th domino has been
# pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# 
# Return a string representing the final state. 
# 
# Example 1:
# 
# 
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# 
# 
# Example 2:
# 
# 
# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.
# 
# 
# Note:
# 
# 
# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'
# 
# 
#
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        l = 0
        r = l
        dominoes = list(dominoes)
        while l < len(dominoes):
            if r >= len(dominoes):
                    break
            if dominoes[r] == '.':
                r += 1
            elif dominoes[r] == 'L':
                if dominoes[l] != 'R':
                    for k in range(l, r):
                        dominoes[k] = 'L'
                else:
                    t = int((r - l - 1) % 2)
                    if t == 0:
                        end = l + int((r - l - 1) / 2) + 1
                        for k in range(l, end):
                            dominoes[k] = 'R'
                        start = l + int((r - l - 1) / 2) + 1
                        for k in range(start, r + 1):
                            dominoes[k] = 'L'
                    else:
                        end = l + int((r - l - 1) / 2)
                        for k in range(l, end + 1):
                            dominoes[k] = 'R'
                        start = l + int((r - l - 1) / 2) + 2
                        for k in range(start, r):
                            dominoes[k] = 'L'
                l = r + 1
                r = l
            else:
                if dominoes[l] == 'R':
                    print(l, r)
                    for k in range(l, r):
                        dominoes[k] = 'R'
                l = r
                r += 1
        if l < len(dominoes) and dominoes[l] == 'R' and r == len(dominoes):
            for k in range(l + 1, r):
                dominoes[k] = 'R'
        return ''.join(dominoes)

if __name__ == '__main__':
    s = Solution()
    t = "R.R.L"
    target = "RRR.L"
    print(s.pushDominoes(dominoes=t))
    
