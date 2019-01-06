#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (47.03%)
# Total Accepted:    83K
# Total Submissions: 176.4K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(128)]
        for i in range(len(s)):
            dp[ord(s[i]) - ord('A')] += 1
        has_odd = []
        a = 0
        even_nums = 0
        for i in range(len(dp)):
            if dp[i] % 2 == 0:
                even_nums += dp[i]
            else:
                a = 1
                has_odd.append(dp[i])
        ans = even_nums + sum(has_odd) - (0 if len(has_odd) == 1 else len(has_odd))
        return ans if ans % 2 != 0 else ans + a


if __name__ == '__main__':
    s = Solution()
    t = "bananas"
    t1 = "aaabddccc"
    print(s.longestPalindrome(s=t1))
    
