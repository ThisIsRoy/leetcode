# Super interesting algorithm for moving in place

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first_zero = 0 # index for moving the non-zero to 
        for idx, num in enumerate(nums):
            if num != 0:
                nums[idx], nums[first_zero] = (nums[first_zero], nums[idx])
                first_zero += 1