#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (25.54%)
# Total Accepted:    670.1K
# Total Submissions: 2.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        a = 0
        b = 1
        len_s = len(s)
        max_len = 1
        while b < len_s:
            if s[b] not in s[a: b]:
                max_len = max(max_len, b - a + 1)
                b += 1
            elif a == b:
                b += 1
            elif s[b] in s[a: b]:
                a += 1
        return max_len

    def lengthOfLongestSubstringWithHash(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_arr = [[0, 0] for i in range(100)]
        maxLen = 0
        l = 0; r = 0
        while r < len(s):
            t = ord(s[r]) - ord(' ')
            if hash_arr[t][1] == 0:
                hash_arr[t] = [r, 1]
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                loc, _ = hash_arr[t]
                for j in range(l, loc + 1):
                    hash_arr[ord(s[j]) - ord(' ')] = [0, 0]
                l = loc + 1
                hash_arr[t] = [r, 1]
                maxLen = max(maxLen, r - l + 1)
                r += 1
        return maxLen