class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numLen = len(nums)
        res = 0
        if (numLen < 2):
            return numLen
        for i in range(numLen):
            cnt = 1
            while nums[i] != i and nums[i] != nums[nums[i]]:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
                cnt += 1
            res = max(res, cnt)
        return res 


if __name__ == '__main__':
    s = Solution()
    print(s.arrayNesting([5,4,0,3,1,6,2]))
    
