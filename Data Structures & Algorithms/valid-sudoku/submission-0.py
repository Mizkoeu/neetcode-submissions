class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        groups = defaultdict(set)
        n = len(board)
        m = len(board[0])

        for r in range(n):
            for c in range(m):
                char = board[r][c]
                if char == '.':
                    continue
                
                if char in row[r] or char in col[c] or char in groups[(r//3)*3 + c//3]:
                    return False

                # add it
                row[r].add(char)
                col[c].add(char)
                groups[(r//3)*3+c//3].add(char)

        return True