class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        if n < 0:
            n *= -1
        n = int(BinaryConversion(n))
        sums = 0
        while n:
            sums += n % 10
            n /= 10
        if sums == 1:
            return True
        return False


def BinaryConversion(n):
    print bin(n)
    return bin(n)[2:]


s = Solution()
print s.isPowerOfTwo(32769)


# 2的n次方，化为二进制后，二进制数首位是1，其余都是0