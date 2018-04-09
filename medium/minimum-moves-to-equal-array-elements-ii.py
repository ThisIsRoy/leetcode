# implements the quick-select algorithm
import math
import random

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = self.quick_select(nums, math.ceil(len(nums) / 2.0))
        return sum([abs(move - median) for move in nums])
        
    def quick_select(self, arr, k):
        pivot = random.choice(arr)
        A1, A2 = list(), list()
        
        for num in arr:
            if num < pivot:
                A1.append(num)
                
            elif num > pivot:
                A2.append(num)
                
        if k <= len(A1):
            return self.quick_select(A1, k)
        
        elif k > len(arr) - len(A2):
            return self.quick_select(A2, k - (len(arr) - len(A2)))
        
        else:
            return pivot