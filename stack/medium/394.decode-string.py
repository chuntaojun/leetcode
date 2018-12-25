#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (43.07%)
# Total Accepted:    79K
# Total Submissions: 183.3K
# Testcase Example:  '"3[a]2[bc]"'
#
# 
# Given an encoded string, return it's decoded string.
# 
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# 
# Examples:
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
#
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        t_1 = ['']
        t_2 = []
        pre_char_is_digit = False
        pre_char_is_s_left = False
        s_left = '['; s_right = ']'
        for i in range(len(s)):
            if s[i] != s_right:
                ascii_num = ord(s[i]) - ord('0')
                if ascii_num >= 0 and ascii_num <= 9:
                    if pre_char_is_digit:
                        t_2.append(t_2.pop() * 10 + ascii_num)
                    else:
                        pre_char_is_digit = True
                        t_2.append(ascii_num)
                else:
                    pre_char_is_digit = False
                    if s[i] == s_left:
                        pre_char_is_s_left = True
                        t_1.append(s_left)
                    else:
                        if not pre_char_is_s_left:
                            t_1.append(t_1.pop() + s[i])
                        else:
                            t_1.append(s[i])
                        pre_char_is_s_left = False

            else:
                if len(t_1) != 0:
                    t_s = []
                    while t_1[-1] != s_left:
                        t_s.append(t_1.pop())
                    t_s.reverse()
                    t_s = ''.join(t_s)
                    t_1.pop()
                    k = t_2.pop()
                    _s = ''
                    while k != 0:
                        _s += t_s
                        k -= 1
                    if len(t_1) != 0 and t_1[-1] != s_left:
                        t_1.append(t_1.pop() + _s)
                    else:
                        t_1.append(_s)
        return (''.join(t_1))


if __name__ == '__main__':
    s = Solution()
    t_s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(s.decodeString(s=t_s))
