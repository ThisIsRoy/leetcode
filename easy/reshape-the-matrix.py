from itertools import chain

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        orig_r = len(nums)
        orig_c = len(nums[0])
        if orig_r * orig_c != r * c:
            return nums
        
        data = list(chain.from_iterable(nums))
        row_range = [i * c for i in range(r)]
        return [data[x:x + c] for x in row_range]