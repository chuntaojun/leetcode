class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        lateral = 1
        vertical = 1
        road = [[r0, c0]]
        r0_t = r0
        c0_t = c0
        if 0 <= R <= 100 and 0 <= C <= 100:
            if 0 <= r0 < R and 0 <= c0 < C:

                max_grid_num = R * C

                direction = [0, 1, 2, -1, -2]
                index = 1
                total_road_len = 0
                while len(road) < max_grid_num:
                    road_tmp = None
                    _dir = direction[index]
                    if _dir == 1 or _dir == -1:
                        road_tmp, r0_t, c0_t = self.draw_guiji(
                            r=r0_t, c=c0_t, lateral=lateral, vertical=None, dir_type=int(_dir / 1), R=R, C=C)
                        lateral += 1
                    elif _dir == 2 or _dir == -2:
                        road_tmp, r0_t, c0_t = self.draw_guiji(
                            r=r0_t, c=c0_t, lateral=None, vertical=vertical, dir_type=int(_dir / 2), R=R, C=C)
                        vertical += 1
                        if _dir == -2:
                            index = 0
                    index += 1
                    road.extend(road_tmp)
        return road

    def draw_guiji(self, r, c, lateral, vertical, dir_type, R, C):
        road = []
        if vertical is None:
            for item in range(1, lateral + 1):
                c += dir_type * 1
                if r >= R or r < 0 or c >= C or c < 0:
                    continue
                road.append([r, c])
        if lateral is None:
            for item in range(1, vertical + 1):
                r += dir_type * 1
                if r >= R or r < 0 or c >= C or c < 0:
                    continue
                road.append([r, c])
        return road, r, c


if __name__ == '__main__':
    s = Solution()
    print(s.spiralMatrixIII(R=1, C=4, r0=0, c0=0))
