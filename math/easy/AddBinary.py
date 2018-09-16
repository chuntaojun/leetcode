class Solution(object):
    def addBinary(self, a, b):
        a, b = StringsChange(a, b)
        temp = 0
        max_size, min_size = Size(len(a), len(b))
        nums = []
        while max_size >= 0:
            while min_size >= 0:
                temp += int(a[max_size]) + int(b[min_size])
                nums.append(temp % 2)
                if max_size + max_size == 0 and temp >= 2:
                    nums.append(1)
                temp = temp / 2
                min_size -= 1
                max_size -= 1
            if max_size < 0:
                break
            if max_size == 0 and temp + int(a[max_size]) == 2:
                nums.append(0)
                nums.append(1)
            elif int(a[max_size]) + temp == 2:
                temp = 1
                nums.append(0)
            elif temp + int(a[max_size]) < 2:
                nums.append(int(a[max_size]) + temp)
                temp = 0
            max_size -= 1
        print nums
        nums.reverse()
        return ''.join(map(str, nums))


def StringsChange(a, b):
    if len(a) > len(b):
        return a, b
    return b, a


def Size(x, y):
    return x - 1, y - 1
