"""
模拟扫雷游戏，摁下指定的位置后的反应
深度优先，恩照题目的意思，只有摁下的是空位且周围也没有雷的时候才需要递归
如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。

"""


class Solution(object):
    def find_mine_num(self, board, x, y, row, col):
        count = 0
        x_bias = [-1, 1, 0, 0, -1, -1, 1, 1]
        y_bias = [0, 0, -1, 1, -1, 1, -1, 1]
        for i in range(len(x_bias)):
            if 0 <= x + x_bias[i] < row and 0 <= y + y_bias[i] < col:
                if board[x + x_bias[i]][y + y_bias[i]] == 'M':
                    count += 1
        return count

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row = len(board)
        col = len(board[0])
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        def dfs(x, y):
            if board[x][y] == 'E':
                mine_num = self.find_mine_num(board, x, y, row, col)
                if mine_num == 0:
                    board[x][y] = 'B'
                    # 递归揭露
                    x_bias = [-1, 1, 0, 0, -1, -1, 1, 1]
                    y_bias = [0, 0, -1, 1, -1, 1, -1, 1]
                    for i in range(len(x_bias)):
                        if 0 <= x + x_bias[i] < row and 0 <= y + y_bias[i] < col:
                            dfs(x + x_bias[i], y + y_bias[i])

                else:
                    board[x][y] = str(mine_num)

        dfs(click[0], click[1])
        return board


board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]
click = [3, 0]
Solution_updateBoard = Solution()
print(Solution_updateBoard.updateBoard(board, click))
