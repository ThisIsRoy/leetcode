# Uses input list itself to keep track of duplicates
# Modifies input however 

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup.append(abs(num))
                
            else:
                nums[abs(num) - 1] *= -1
                
        return dup