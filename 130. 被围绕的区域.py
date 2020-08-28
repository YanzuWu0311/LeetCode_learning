"""
一个方阵由“X”“O”组成，把被围住的“O”替换成“X”
深度优先，遍历，从边界上的“O”开始，把与之相连的“O”打个标签，没打标签的“O”都要被替换
"""


# 任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:  # 若给定的board是空的
            return
        row_num = len(board)
        col_num = len(board[0])

        def dfs(x, y):  # 尽力找与已知是‘O’的点相连的点，并标记
            # x.y不能越界，且对应是‘O’时才处理
            if not 0 <= x < row_num or not 0 <= y < col_num or board[x][y] != 'O':
                return
            board[x][y] = 'No_Need_change'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(row_num):
            dfs(i, 0)
            dfs(i, col_num - 1)
        for i in range(col_num):
            dfs(0, i)
            dfs(row_num - 1, i)
        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] == 'No_Need_change':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        # return board


board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
]
Solution_solve = Solution()
print(Solution_solve.solve(board))
