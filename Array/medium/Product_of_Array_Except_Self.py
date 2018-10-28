class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 1
        zerosNum = len([i for i in nums if i == 0])
        print(zerosNum)
        if zerosNum <= 1:
            for i in nums:
                if i != 0:
                    tmp *= i
        elif zerosNum > 1:
            return [0 for i in nums]
        answer = []
        for i in nums:
            if i != 0 and zerosNum == 0:
                answer.append(int(tmp / i))
            elif i != 0 and zerosNum != 0:
                answer.append(0)
            else:
                answer.append(tmp)
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    
