class Solution(object):
    def isHappy(self, n):
        temp = []
        while True:
            ans = NumberToList(n)
            n = 0
            for i in range(len(ans)):
                n += ans[i] * ans[i]
            temp.append(n)
            if n == 1:
                return True
            else:
                for j in range(0, len(temp) - 1):
                    if n == temp[j]:
                        return False


def NumberToList(n):
    ans = []
    while n:
        ans.append(n % 10)
        n /= 10
    return ans


print Solution().isHappy(7)
