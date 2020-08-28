"""
一开始给一个起始点，将其染色，同时和原先起始点相同颜色的并且在起始点上左下右四个邻近点也染色，同时这些新染色的周围也一样处理
深度优先，用一个tag矩阵去标记哪些需要染色，从起始点开始，遍历其上左下右，同时遍历到其中一点时也要遍历其上左下右，递归执行
"""


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        def dfs(x, y):
            tag[x][y] = 1
            if y + 1 < col and image[x][y + 1] == image[x][y] and tag[x][y + 1] == 0:
                dfs(x, y + 1)
            if y - 1 >= 0 and image[x][y - 1] == image[x][y] and tag[x][y - 1] == 0:
                dfs(x, y - 1)
            if x + 1 < row and image[x + 1][y] == image[x][y] and tag[x + 1][y] == 0:
                dfs(x + 1, y)
            if x - 1 >= 0 and image[x - 1][y] == image[x][y] and tag[x - 1][y] == 0:
                dfs(x - 1, y)

        row = len(image)
        col = len(image[0])
        tag = [[0] * col for i in range(row)]  # 用来标记哪些需要更改值
        if image[sr][sc] == newColor:  # 若一开始就不需要染色，直接返回
            return image
        else:
            dfs(sr, sc)
            for i in range(row):
                for j in range(col):
                    if tag[i][j] == 1:
                        image[i][j] = newColor
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
Solution_floodFill = Solution()
print(Solution_floodFill.floodFill(image, sr, sc, newColor))
