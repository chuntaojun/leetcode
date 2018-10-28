class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        answer = []
        times = 1
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if times == 2:
                    answer.append(nums[i])
            elif nums[i + 1] != nums[i]:
                if times == 2:
                    answer.append(nums[i])
                    times = 1
            elif nums[i + 1] == nums[i]:
                times += 1
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4,3,2,7,8,2,3,1]))
    
