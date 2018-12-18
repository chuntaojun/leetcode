#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (27.56%)
# Total Accepted:    133.4K
# Total Submissions: 484K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it. 
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# path = "/a/../../b/../c//.//", => "/c"
# path = "/a//b////c/d//././/..", => "/a/b/c"
# 
# In a UNIX-style file system, a period ('.') refers to the current directory,
# so it can be ignored in a simplified path. Additionally, a double period
# ("..") moves up a directory, so it cancels out whatever the last directory
# was. For more information, look here:
# https://en.wikipedia.org/wiki/Path_(computing)#Unix_style
# 
# Corner Cases:
# 
# 
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# 
# 
#
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        file_path = []
        s = path.split('/')
        for i in range(len(s)):
            if s[i] == '':
                continue
            elif s[i] == '.':
                continue
            elif s[i] == '..':
                if len(file_path) == 0:
                    file_path.append('/')
                file_path.pop()
            else:
                file_path.append(s[i])
        return '/' + '/'.join(file_path)


if __name__ == '__main__':
    s = Solution()
    t = "/home//foo/"
    print(s.simplifyPath(path=t))
