from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        boxes = {}
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if i >= len(rows):
                    rows.append(defaultdict(lambda: 0))
                rows[i][board[i][j]] += 1
                if j >= len(cols):
                    cols.append(defaultdict(lambda: 0))
                cols[j][board[i][j]] += 1
                if (i // 3, j // 3) not in boxes:
                    boxes[(i // 3, j // 3)] = defaultdict(lambda: 0)
                boxes[(i // 3, j // 3)][board[i][j]] += 1
        
        for row in rows:
            for i in range(1, 10):
                if row[str(i)] > 1:
                    return False
        for col in cols:
            for j in range(1, 10):
                if col[str(j)] > 1:
                    return False
        for k, v in boxes.items():
            for k in range(1, 10):
                if v[str(k)] > 1:
                    return False
        
        return True