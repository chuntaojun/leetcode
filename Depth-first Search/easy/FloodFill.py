"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor,
"flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
"""

import sys

sys.setrecursionlimit(1000000)


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        wight, length = len(image), len(image[0])
        oldColor = image[sr][sc]
        for i in range(wight):
            for j in range(length):
                if image[i][j] == oldColor and image[i][j] != newColor:
                    self.DFS(image, newColor, sr, sc, oldColor)
        return image

    def DFS(self, image, newColor, i, j, oldColor):
        if i < 0 or i >= len(image):
            return
        if j < 0 or j >= len(image[0]):
            return
        if image[i][j] != oldColor:
            return
        image[i][j] = newColor

        def fill_color(_image, _i, _j):
            if _i < 0 or _i >= len(image):
                return
            if _j < 0 or _j >= len(image[0]):
                return
            if _image[i][j] != oldColor:
                return
            _image[i][j] = newColor

        fill_color(image, i, j + 1)
        fill_color(image, i, j - 1)
        fill_color(image, i + 1, j)
        fill_color(image, i - 1, j)
        self.DFS(image, newColor, i, j + 1, oldColor)
        self.DFS(image, newColor, i, j - 1, oldColor)
        self.DFS(image, newColor, i + 1, j, oldColor)
        self.DFS(image, newColor, i - 1, j, oldColor)


if __name__ == '__main__':
    s = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print s.floodFill(image, sr, sc, newColor)
