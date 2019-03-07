#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (45.15%)
# Total Accepted:    47.4K
# Total Submissions: 105K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
# 
# You need to return whether the student could be rewarded according to his
# attendance record.
# 
# Example 1:
# 
# Input: "PPALLP"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "PPALLL"
# Output: False
# 
# 
# 
# 
# 
#
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s += 'P'
        Acount = 0
        for i in range(1, len(s)):
            if s[i - 1] == 'A':
                Acount += 1
                if Acount > 1:
                    return False
            elif s[i - 1] == 'L' and s[i] == 'L' and s[i - 2] == 'L':
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    t = "LLLPPLL"
    print(s.checkRecord(s=t))
    

