# Usage of stack to keep track of only relevant temperatures

from collections import defaultdict

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        stack = [(length - 1, temperatures[-1])]
        temp_inc = [0]
        traversal = range(len(temperatures) - 1)
        traversal.reverse()
        
        for idx in traversal:
            temp = temperatures[idx]
            while stack and temp >= stack[-1][1]:
                stack.pop()
            
            if not stack:
                temp_inc.append(0)
            
            else:
                temp_inc.append(stack[-1][0] - idx)
            
            stack.append((idx, temp))
            
        temp_inc.reverse()
        return temp_inc