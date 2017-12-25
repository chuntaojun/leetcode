class Solution(object):
    def multiply(self, num1, num2):
        def judge(a, b):
            if len(a) > len(b):
                return a, b, 2 * len(a)
            return b, a, 2 * len(b)
        num1, num2, length = judge(num1, num2)
        ans = [0 for i in range(length)]
        length, ans[0] = 0, 0
        for i in range(len(num2) - 1, -1, -1):
            for j in range(len(num1) - 1, -1, -1):
                temp = int(num1[j]) * int(num2[i]) + ans[length]
                ans[length] = temp % 10
                if temp > 9:
                    ans[length + 1] = ans[length + 1] + temp / 10
                length += 1
            length = len(num2) - i
        ans.reverse()
        while True:
            if ans[0] == 0:
                ans.remove(ans[0])
            else:
                break
        return ''.join(map(str, ans))


s = Solution()
print s.multiply("1233", "456")
