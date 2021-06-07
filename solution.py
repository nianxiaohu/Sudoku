class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def box(row, col):
            """Calculate the box index based on row and col
            """
            return row // 3 * 3 + col // 3

        def isValid(row, col, nbr):
            """ Return True if you can place nbr+1 in cell (row, col)
            without compromising the constraint of row, column and box
            """
            box_idx = box(row, col)
            if not (rows[row][nbr] or cols[col][nbr] or grids[box_idx][nbr]):
                return True
            return False

        def place_nbr(row, col, nbr):
            """ When nbr+1 is placed in cell(row, col)
            Respective data structures are updated to reflect changes
            """
            box_idx = box(row, col)
            rows[row][nbr] = True
            cols[col][nbr] = True
            grids[box_idx][nbr] = True
            board[row][col] = str(nbr + 1)

        def remove(row, col, nbr):
            """ Backtrack by removing nbr+1 from cell(row, col)
            Then update data structures to reflect changes
            and setting the board values at respective cell back to '.'
            Is called when following path does not lead to a solution
            """
            rows[row][nbr] = False
            cols[col][nbr] = False
            grids[box(row, col)][nbr] = False
            board[row][col] = 'X'

        def place_next(row, col):
            """ Call backtrack in recursion until it reaches the end of board
            """
            nonlocal solved
            if row == 8 and col == 8:
                solved = True
            else:
                if col == 8:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == 'X':
                for nbr in range(1, 10):
                    nbr -= 1
                    if isValid(row, col, nbr):
                        place_nbr(row, col, nbr)
                        place_next(row, col)

                        if not solved:
                            remove(row, col, nbr)
            else:
                place_next(row, col)

        # set up data structure to enforce constraint and read in the original board information
        rows = {i: [False] * 9 for i in range(9)}
        cols = {i: [False] * 9 for i in range(9)}
        grids = {i: [False] * 9 for i in range(9)}
        for row in range(9):
            for col in range(9):
                if board[row][col] != 'X':
                    nbr = int(board[row][col])
                    nbr -= 1
                    rows[row][nbr] = True
                    cols[col][nbr] = True
                    grids[box(row, col)][nbr] = True

        solved = False
        backtrack()
        return board
