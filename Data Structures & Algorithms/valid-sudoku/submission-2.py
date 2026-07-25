class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blocks = [0] * 9
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                bit = 1 << int(num)
                block_idx = (r // 3) * 3 + (c // 3)
                if (rows[r] & bit) or (cols[c] & bit) or (blocks[block_idx] & bit):
                    return False
                
                rows[r] |= bit
                cols[c] |= bit
                blocks[block_idx] |= bit
        
        return True