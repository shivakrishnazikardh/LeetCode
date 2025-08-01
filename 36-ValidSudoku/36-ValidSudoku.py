# Last updated: 7/28/2025, 2:18:37 PM
class Solution(object):
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == "." :
                    continue
                if (board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in square[i//3, j//3]) :
                   return False
                
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                square[i//3, j//3].add(board[i][j])
                
        return True
        