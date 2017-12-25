class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        temp_str_1 = a.split('+')
        temp_str_2 = b.split('+')
        temp_str_1 = map(int, [temp_str_1[0], temp_str_1[1].split('i')[0]])
        temp_str_2 = map(int, [temp_str_2[0], temp_str_2[1].split('i')[0]])
        ans_a = temp_str_1[0] * temp_str_2[0]
        ans_b = temp_str_1[0] * temp_str_2[1] + temp_str_1[1] * temp_str_2[0]
        ans_c = temp_str_1[1] * temp_str_2[1]
        return str(ans_a + ans_c * -1) + '+' + str(ans_b) + 'i'


if __name__ == '__main__':
    s = Solution()
    print s.complexNumberMultiply("1+-1i", "1+-1i")
