#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (62.31%)
# Total Accepted:    103K
# Total Submissions: 165.3K
# Testcase Example:  '"Let\'s take LeetCode contest"'
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.
# 
#
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = ''
        ans= []
        for i in range(len(s)):
            if s[i] == ' ':
                ans.append(t)
                t = ''
                ans.append(s[i])
            else:
                t = s[i] + t
        ans.append(t)
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    t = "Let\'s take LeetCode contest"
    print(s.reverseWords(s=t))
    
