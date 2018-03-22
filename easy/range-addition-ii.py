# This optimal solution solves the math problem, whereas the brute force solution is about the technical programming

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
### Brute force solution
#         if ops == []:
#             return m * n
#         elif len(ops) == 1:
#             return ops[0][0] * ops[0][1]
        
#         matrix = [[0 for _ in range(n)] for _ in range(m)]
        
#         for op in ops:
#             for row in range(op[0]):
#                 for col in range(op[1]):
#                     matrix[row][col] += 1
        
#         max_val = max([max(x) for x in matrix])
#         max_num = 0
        
#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 if matrix[row][col] == max_val:
#                     max_num += 1
        
#         return max_num

        if ops == []:
            return m * n
        
        return min([row[0] for row in ops]) * min([col[1] for col in ops])