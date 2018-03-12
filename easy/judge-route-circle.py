class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # define right and up as positive, left and down as negative
        position = [0, 0]
        
        robot_move = self.robot_move_dict()
        
        for move in moves:
            axis = robot_move[move][0]
            direction = robot_move[move][1]
            position[axis] += direction
            
        return True if position == [0, 0] else False 
    
    def robot_move_dict(self):
        return {'R': (0, 1), 'L': (0, -1), 'U': (1, 1), 'D': (1, -1)}