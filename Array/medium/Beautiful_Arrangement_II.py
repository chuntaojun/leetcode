class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        answer = []
        i, j = 1, n
        while (i <= j):
            if k > 1:
                if k % 2 == 1:
                    answer.append(i)
                    i += 1
                else:
                    answer.append(j)
                    j -= 1
                k -= 1
            else:
                answer.append(i)
                i += 1
        return answer

if __name__ == '__main__':
    pass
