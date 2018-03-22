import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        length = math.sqrt(area)
            
        if not length.is_integer():
            length = math.floor(length)
            
        while not (float(area) / length).is_integer():
            length -= 1
        
        width = area / length
        return [int(width), int(length)]