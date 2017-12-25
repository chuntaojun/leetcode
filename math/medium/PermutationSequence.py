class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = [1]
        for i in range(1, n + 1):
            temp.append(temp[-1] * i)
        ans, number = [], [i for i in range(1, n + 1)]
        for i in range(n):
            digit = (k - 1) / temp[n - i - 1]
            ans.append(number[digit])
            number.remove(number[digit])
            k = (k - 1) % temp[n - i - 1] + 1
        return "".join(map(str, ans))


if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(4, 8)
