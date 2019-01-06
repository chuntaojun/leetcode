import sys

class Solution(object):
    def __init__(self, *args, **kwargs):
        self.t = []
        self.ans = []

    def func(self, target, n, l):
        if len(n) <= 0:
            return
        if target == n[-1] and len(self.t) == l - 1:
            self.t.append(n[-1])
            print(self.t)
            self.t.pop()
        self.t.append(n[-1])
        self.func(target=target - n[-1], n=n[:len(n) - 1], l=l)
        self.t.pop()
        self.func(target=target, n=n[:len(n) - 1], l=l)


if __name__ == '__main__':
    s = Solution()
    n = [-1,0,1,2,-1,-4]
    s.func(target=0, n=n, l=3)
