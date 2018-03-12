# Brute force solution
# Room for improvement 

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        
        peri = 0 
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    peri += 4
                    
                    if row > 0 and grid[row - 1][col]:
                        peri -= 1

                    if row < rows - 1 and grid[row + 1][col]:
                        peri -= 1

                    if col > 0 and grid[row][col - 1]:
                        peri -= 1

                    if col < cols - 1 and grid[row][col + 1]:
                        peri -= 1
                    
        return peri 