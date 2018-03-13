# Brute force solution
# Use dictionary to keep track of which ships are which 

from collections import defaultdict


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if board == []:
            return 0
        
        ship_dict = defaultdict(lambda: defaultdict(int))
        ship_count = 1
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'X' and not ship_dict[row][col]:
                    
                    # check left
                    if row > 0 and ship_dict[row - 1][col]:
                        ship_dict[row][col] = ship_dict[row - 1][col]
                    
                    # check right
                    elif row < rows - 1 and ship_dict[row + 1][col]:
                        ship_dict[row][col] = ship_dict[row + 1][col]
                        
                    # check above
                    elif col > 0 and ship_dict[row][col - 1]:
                        ship_dict[row][col] = ship_dict[row][col - 1]
                        
                    # check below 
                    elif col < cols - 1 and ship_dict[row][col + 1]:
                        ship_dict[row][col] = ship_dict[row][col + 1]
                        
                    # new ship 
                    else:
                        ship_dict[row][col] = ship_count
                        ship_count += 1
                        
        return ship_count - 1 
                    