class Solution(object):
    def plusOne(self, digits):
        length = len(digits)
        print length
        if length == 0:
            return [1]
        plus = 0
        digits[length - 1] += 1
        while length > 0:
            digits[length - 1] += plus
            if digits[length - 1] > 9:
                digits[length - 1], plus = 0, 1
            else:
                plus = 0
                break
            length -= 1
        if plus == 0:
            return digits
        digits.insert(0, 1)
        return digits


def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return []
    return [int(number) for number in input.split(",")]


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    if not len_of_list:
        return "[]"

    result = ""
    for index in range(len_of_list):
        num = nums[index]
        result += str(num) + ", "
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            digits = stringToIntegerList(line)

            ret = Solution().plusOne(digits)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
