class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(A[i] - i) >= 2: return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isIdealPermutation([1,0,2]))
