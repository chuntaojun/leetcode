class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        finalTime = duration
        if len(timeSeries) == 0:
            return 0
        if len(timeSeries) == 1:
            return duration
        for i in range(1, len(timeSeries)):
            timeMisc = timeSeries[i] - timeSeries[i - 1]
            if timeMisc >= duration:
                finalTime += duration
            if timeMisc < duration:
                finalTime += timeMisc
        return finalTime


if __name__ == '__main__':
    s = Solution()
    print(s.findPoisonedDuration([1,2], 2))

