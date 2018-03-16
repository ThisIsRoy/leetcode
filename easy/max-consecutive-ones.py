# Be careful about edge cases where there are only 1s in the list

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
                
            else:
                max_ones = max(max_ones, ones)
                ones = 0
        
        max_ones = max(ones, max_ones)
        return max_ones
            