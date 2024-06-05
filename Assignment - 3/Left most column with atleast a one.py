class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        current_row = 0
        current_col = cols - 1
        leftmost_col = -1
        
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 1:
                leftmost_col = current_col
                current_col -= 1
            else:
                current_row += 1
        
        return leftmost_col
