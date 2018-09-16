class Solution(object):
    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s * x`[::-1])
        return s * r * (r < 2 ** 31)

    # def reverse_my(self, x):
    #     num_type = 1
    #     if x > 0:
    #         temp = x
    #     else:
    #         temp = -1 * x
    #         num_type = -1
    #     reverse_num = 0
    #     while temp != 0:
    #         b = temp % 10
    #         reverse_num = reverse_num * 10 + b
    #         temp /= 10
    #     if reverse_num < 2 ** 31:
    #         return reverse_num * num_type
    #     return 0


# 链表的逆序
