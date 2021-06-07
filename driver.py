from solution import Solution
3
for i in range(1, 6):
    puzzle = []
    with open('puzzle{i}.txt'.format(i=i)) as f:
        for line in f.readlines():
            puzzle.append([c for c in line])
    sudoku = Solution()
    sudoku.solveSudoku(puzzle)
    with open('puzzle{i}.sln.txt'.format(i=i), 'w') as f:
        for row in puzzle:
            f.write("".join(row))