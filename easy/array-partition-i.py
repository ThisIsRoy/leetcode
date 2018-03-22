class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pair_sum = 0
        
        for idx in range(1, len(nums), 2):
            pair_sum += nums[idx - 1]
            
        return pair_sum