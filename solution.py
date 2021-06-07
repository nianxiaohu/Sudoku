class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # calculate the box index
        def box(row, col):
            return row // 3 * 3 + col // 3

        def isValid(row, col, nbr):
            box_idx = box(row, col)
            if not (rows[row][nbr] or cols[col][nbr] or grids[box_idx][nbr]):
                return True
            return False

        def place_nbr(row, col, nbr):
            box_idx = box(row, col)
            rows[row][nbr] = True
            cols[col][nbr] = True
            grids[box_idx][nbr] = True
            board[row][col] = str(nbr + 1)

        def remove(row, col, nbr):
            rows[row][nbr] = False
            cols[col][nbr] = False
            grids[box(row, col)][nbr] = False
            board[row][col] = '.'

        def place_next(row, col):
            nonlocal solved
            if row == 8 and col == 8:
                solved = True
            else:
                if col == 8:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for nbr in range(1, 10):
                    nbr -= 1
                    if isValid(row, col, nbr):
                        place_nbr(row, col, nbr)
                        place_next(row, col)

                        if not solved:
                            remove(row, col, nbr)
            else:
                place_next(row, col)

        rows = {i: [False] * 9 for i in range(9)}
        cols = {i: [False] * 9 for i in range(9)}
        grids = {i: [False] * 9 for i in range(9)}
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    nbr = int(board[row][col])
                    nbr -= 1
                    rows[row][nbr] = True
                    cols[col][nbr] = True
                    grids[box(row, col)][nbr] = True

        solved = False
        backtrack()
        return board
