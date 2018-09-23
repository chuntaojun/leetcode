class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import heapq
        if n <= 1:
            return n

        n -= 1
        key = [2, 3, 5]
        h = []
        for i in range(3):
            heapq.heappush(h, (key[i], i))
        value = key[0]
        while n > 0:
            value, level = heapq.heappop(h)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(h, (new_value, level))
                level += 1
            n -= 1
        return value


s = Solution()
print(s.nthUglyNumber(9))
