# Clever use of negative values
# Be careful of correct index values!

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """   
        # if they appear make their corresponding index negative
        for num in nums:
            nums[abs(num) - 1] = -1 * abs(nums[abs(num) - 1])
            
        return [idx + 1 for idx, num in enumerate(nums) if num > 0]