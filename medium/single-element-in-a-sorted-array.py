class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
            
        
        mid = len(nums) / 2
        
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        
        elif mid % 2 == 0:
            # single num is on the left
            if nums[mid] == nums[mid - 1]:
                return self.singleNonDuplicate(nums[: mid  + 1])
            
            # single num is on right
            else:
                return self.singleNonDuplicate(nums[mid:])
            
        else:
            if nums[mid] == nums[mid - 1]:
                # single num is on right
                return self.singleNonDuplicate(nums[mid + 1:])
            
            # single num is on left
            else:
                return self.singleNonDuplicate(nums[: mid ])