# Dynamic Programming Solution!

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for layer in range(len(triangle) - 2, -1, -1):
            for val in range(len(triangle[layer])):
                triangle[layer][val] += min(triangle[layer+1][val], triangle[layer+1][val+1])
                
        return triangle[0][0]
<<<<<<< HEAD
        
=======
        
>>>>>>> 7a155c2dbb8eae28b188f1678143f27323e8eb21
