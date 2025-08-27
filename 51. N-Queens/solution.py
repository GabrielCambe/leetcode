class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        
        # The solution can be repreented by a single array of length n, where the value at index i is the column of the queen in the ith row.
        board = [None]*n
        
        def backtrack(board):
            pass
        
        for i in range(n):
            board[0] = i
            backtrack(board)
        
        return [toString(b) for b in solutions]
