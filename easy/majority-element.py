# First solution uses hash map, but isn't as clever or fast as the second solution
# Second solution is the Boyer algorithm

#from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         half_len = len(nums) / 2
#         for num, count in Counter(nums).items():
#             if count > half_len:
#                 return num
        
        count = 0
        for num in nums:
            if count == 0:
                major = num
                count += 1
                
            elif num == major:
                count += 1

            else:
                count -= 1
        
        return major