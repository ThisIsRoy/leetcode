# Modified BFS approach 

from collections import defaultdict

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        
        visited = defaultdict(lambda: False)
        queue = []
        rows = len(grid)
        cols = len(grid[0])
        max_island = 0
        
        # iterate through all values in grid
        for row in range(rows):
            for col in range(cols):
                
                coord = (row, col)
                
                # run bfs on island if not visited 
                if not visited[coord] and grid[row][col]:
                    
                    island = 0
                    queue.append(coord)
                    visited[coord] = True
                    
                    while queue:
                        curr = queue.pop(0)
                        island += 1
                        x_val = curr[0]
                        y_val = curr[1]
                        
                        if x_val > 0 and not visited[(x_val - 1, y_val)] and grid[x_val -1][y_val]:
                            queue.append((x_val - 1, y_val))
                            visited[(x_val - 1, y_val)] = True
                            
                        if x_val < rows - 1 and not visited[(x_val + 1, y_val)] and grid[x_val + 1][y_val]:
                            queue.append((x_val + 1, y_val))
                            visited[(x_val + 1, y_val)] = True
                            
                        if y_val > 0 and not visited[(x_val, y_val - 1)] and grid[x_val][y_val - 1]:
                            queue.append((x_val, y_val - 1))
                            visited[(x_val, y_val - 1)] = True

                        if y_val < cols - 1 and not visited[(x_val, y_val + 1)] and grid[x_val][y_val + 1]:
                            queue.append((x_val, y_val + 1))
                            visited[(x_val, y_val + 1)] = True
                    
                    max_island = max(max_island, island)
                    
        return max_island
        
        