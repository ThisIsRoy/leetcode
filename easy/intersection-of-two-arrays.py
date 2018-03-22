# Note: a one line solution is "return list(set(nums1).intersection(set(nums2)))"
# I chose to implement algorithm instead for practice and for faster runtime (why though)

from collections import defaultdict

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_dict = defaultdict(lambda: False)
        
        for num in nums1:
            num_dict[num] = True
            
        intersect = []
        
        for num in nums2:
            if num_dict[num]:
                intersect.append(num)
                num_dict[num] = False
                
        return intersect