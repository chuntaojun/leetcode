from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, n):
        """
        :type N: int
        :rtype: bool
        """
        t = 1
        cands = set()
        while t <= 1000000000:
            tt = sorted([ttt for ttt in str(t)])
            cands.add(''.join(tt))
            t *= 2

        tt = sorted([ttt for ttt in str(n)])
        return ''.join(tt) in cands
