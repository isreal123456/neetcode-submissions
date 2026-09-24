class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for x in range(9):
            row = [board[x][i] for i in range(9) if board[x][i] != "."]
            if len(row) != len(set(row)):
                return False
            col = [board[i][x] for i in range(9) if board[i][x] != "."]
            if len(col) != len(set(col)):
                return False     
            
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                box = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] != ".":
                            box.append(board[i][j])

                if len(box) != len(set(box)):
                    return False
        return True