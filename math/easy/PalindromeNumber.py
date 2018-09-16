class Solution(object):
    def isPalindrome(self, x):
        if str(x) == `x`[::-1]:
            return True
        return False


s = Solution()
print s.isPalindrome(1223221)


# 判断是不是回文串