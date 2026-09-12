
class Solution:

    # Helper function to return a list of all numbers in a square on the board
    def getSudokuSquare(self, board: List[List[str]], square: int) -> List[str]:

        # Determine index of the top left board square
        topleft_row = (square // 3) * 3
        topleft_col = (square % 3) * 3

        # Create list to store all entries in square
        square_entries = []
        
        # Loop through all entries 
        for i in range(3):
            row_section = board[topleft_row + i][topleft_col:topleft_col+3]
            square_entries.extend(row_section)

        return square_entries

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check validity of rows
        for i in range(0, 9):
            row = board[i]

            seen = set()
            for entry in row:
                # If we have already seen the number, return false
                if entry != '.' and entry in seen:
                    return False
                seen.add(entry)
        
        # Check validity of cols
        for i in range(0,9):
            col = [board[row_i][i] for row_i in range(0,9)]

            seen = set()
            for entry in col:
                # If already seen, return false
                if entry != '.' and entry in seen:
                    return False
                seen.add(entry)

        # Check validity of squares
        for i in range(0,9):
            square = self.getSudokuSquare(board, i)

            seen = set()
            for entry in square:
                # If already seen, return false
                if entry != '.' and entry in seen:
                    return False
                seen.add(entry)

        return True
    
            



  




        