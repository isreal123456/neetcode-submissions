class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            nums = [n for n in row if n != "."]
            if len(nums) != len(set(nums)):
                return False

        for col in range(9):
            nums = [board[row][col] for row in range(9)
                    if board[row][col] != "."]
            if len(nums) != len(set(nums)):
                return False

        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                nums = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != ".":
                            nums.append(board[i][j])

                if len(nums) != len(set(nums)):
                    return False

        return True