"""Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules."""
from collections import defaultdict
from typing import List

class Solution:
    def get_square(self,n):
        if n < 3:
            return 0
        if n < 6:
            return 1
        return 2

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        squares = defaultdict(list)
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                k, l = self.get_square(i), self.get_square(j)
                if col not in cols[j] and col not in rows[i] and col not in squares[(k,l)]:
                    rows[i].append(col)
                    cols[j].append(col)
                    squares[(k,l)].append(col)
                else:
                    return False
        return True
