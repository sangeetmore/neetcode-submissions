class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_cols=defaultdict(set)
        seen_rows=defaultdict(set)
        seen_square=defaultdict(set)

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val == '.':
                    continue
                if (val in seen_rows[r] or val in seen_cols[c] or val in seen_square[(r//3),(c//3)]):
                    return False
                seen_rows[r].add(val)
                seen_cols[c].add(val)
                seen_square[(r//3),(c//3)].add(val)
        return True
                

             