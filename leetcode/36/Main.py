# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            return True

        def is_valid_column(board):
            # zip() 返回由這些元組組成的列表
            # * 是將 array 轉換成 zip 的參數, 像是 zip([], [], [])
            # print(*board)
            # print("---")
            for col in zip(*board):
                if not is_valid(col):
                    return False
            return True

        def is_valid_square(board):
            # 將中間9宮格轉成一個 Array
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i+3)
                              for y in range(j, j+3)]
                    if not is_valid(square):
                        return False
            return True

        def is_valid(value):
            res = [i for i in value if i != '.']
            # print(set(res))
            # print(len(res))
            # set 不會包含重複的資料
            # 用 set 移除重複資料, 跟沒移除的比較, 判斷是否有重複
            return len(res) == len(set(res))

        return is_valid_row(board) and is_valid_column(board) and is_valid_square(board)
