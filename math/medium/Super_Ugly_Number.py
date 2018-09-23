class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        if n <= 1:
            return n
        n -= 1
        h = []
        primelen = len(primes)
        for i in range(primelen):
            heapq.heappush(h, (primes[i], i))
        value = primes[0]
        while n > 0:
            value, level = heapq.heappop(h)
            while level < primelen:
                new_value = primes[level] * value
                heapq.heappush(h, (new_value, level))
                level += 1
            n -= 1
        return value


if __name__ == '__main__':
    pass
    
