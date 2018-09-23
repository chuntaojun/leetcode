class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        points.sort(key=self.first_num)
        print(points)
        first = [points[0], points[1]]
        second = [points[2], points[3]]
        first.sort(key=self.second_num)
        second.sort(key=self.second_num)
        print(first, second)
        a1 = (first[1][0] - second[0][0])
        b1 = (first[1][1] - second[0][1])
        a2 = (first[0][0] - second[1][0])
        b2 = (first[0][1] - second[1][1])
        print(a1, b1, a2, b2)
        c1 = (first[0][0] - first[1][0])
        d1 = (first[0][1] - first[1][1])
        c2 = (first[0][0] - second[0][0])
        d2 = (first[0][1] - second[0][1])
        if (c1 == 0 and d1 != 0 and d2 == 0 and c2 != 0) or (c1 != 0 and d1 == 0 and c2 == 0 and d2 != 0) or (c1 * c2 + d1 * d2 == 0 and c1 + c2 + d1 + d2 != 0):
            if (a1 == 0 and b1 != 0 and a2 != 0 and b2 == 0) or (a1 != 0 and b1 == 0 and a2 == 0 and b2 != 0) or (a1 * a2 + b1 * b2 == 0 and a1 + a2 + b1 + b2 != 0):
                return ((first[1][0] + second[0][0]) == (first[0][0] + second[1][0])) and ((first[1][1] + second[0][1]) == (first[0][1] + second[1][1]))
        return False

            
    def first_num(self, em):
        return em[0]
    
    def second_num(self, em):
        return em[1]
        

if __name__ == '__main__':
    s = Solution()
    print(s.validSquare([1,1]
,[5,3]
,[3,5]
,[7,7]))
    print(s.validSquare([0, 0], [0, 0], [0, 0], [0, 0]))
