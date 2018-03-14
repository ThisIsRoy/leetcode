class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if matrix == []:
            return True
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Check diagonals starting from the left 
        for row in range(rows):
            col = 0
            val = matrix[row][col]
            while col < cols - 1 and row < rows - 1:
                row += 1
                col += 1
                if matrix[row][col] != val:
                    return False
                
        # Check diagonals starting from the top
        for col in range(1, cols):
            row = 0
            val = matrix[row][col]
            while col < cols - 1 and row < rows - 1:
                row += 1
                col += 1
                if matrix[row][col] != val:
                    return False
                
        return True