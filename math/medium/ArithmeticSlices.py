class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = [(A[i + 1] - A[i]) for i in range(len(A) - 1)]
        temp.append(0.5)
        sums, sign, i, count, counts = 0, temp[0], 0, 0, []
        while i < len(temp):
            if temp[i] == sign:
                count += 1
                i += 1
            else:
                if count >= 2:
                    counts.append(count)
                count = 0
                sign = temp[i]
        for i in counts:
            sums += ((i * i) - i) / 2
        return sums


if __name__ == '__main__':
    s = Solution()
    print s.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10])
