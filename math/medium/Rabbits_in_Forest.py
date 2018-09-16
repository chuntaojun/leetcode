class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        _color_map = {}
        rabbits = 0
        for color in answers:
            if color in _color_map:
                _color_map[color] += 1
            else:
                _color_map[color] = 1
        for key, value in _color_map.items():
            rabbits += int((value + key) / (key + 1)) * (key + 1)
        return int(rabbits)


if __name__ == '__main__':
    s = Solution()
    t = [2, 2, 0, 0, 2]
    print(s.numRabbits([0, 0, 1, 1, 1]))
    print(s.numRabbits(t))
