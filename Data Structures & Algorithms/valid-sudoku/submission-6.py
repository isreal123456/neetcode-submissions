class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            n = []
            for h in board[i]:
                if h == ".":
                    continue
                if h in n:
                    return False
                n.append(h)

            m = []
            for h in range(9):
                o = board[h][i]
                if o == ".":
                    continue
                if o in m:
                    return False
                m.append(o)
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                n = []

                for i in range(3):
                    for j in range(3):
                        h = board[r + i][c + j]

                        if h == ".":
                            continue
                        if h in n:
                            return False
                        n.append(h)

        return True