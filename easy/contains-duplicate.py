# Solution very slow however (beats 13%)

from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dict = defaultdict(int)
        
        for num in nums:
            if not num_dict[num]:
                num_dict[num] += 1
            
            else:
                return True
            
        return False