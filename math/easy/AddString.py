class Solution(object):
    def addStrings(self, num1, num2):
        maxSize, minSize = MaxMinSize(num1, num2)
        num1, num2 = ChangeNum1Num2(num1, num2)
        num1.reverse()
        num2.reverse()
        ans = [0 for i in range(maxSize)]
        i, j = 0, 0
        while i < maxSize - 1:
            while j < minSize:
                temp = ans[i] + int(num1[i]) + int(num2[j])
                ans[i] = temp % 10
                ans[i + 1] = temp / 10
                j += 1
                i += 1
            if i >= maxSize - 1:
                break
            temp = ans[i] + int(num1[i])
            ans[i] = temp % 10
            ans[i + 1] = temp / 10
            i += 1
        ans.reverse()
        ans = map(str, ans)
        strs = str(int(''.join(ans)))
        return strs


def MaxMinSize(num1, num2):
    if len(num1) > len(num2):
        return len(num1) + 1, len(num2)
    return len(num2) + 1, len(num1)


def ChangeNum1Num2(num1, num2):
    if len(num1) > len(num2):
        return list(num1), list(num2)
    return list(num2), list(num1)


s = Solution()
print s.addStrings("584", "18")
