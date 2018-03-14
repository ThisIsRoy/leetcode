# There are much faster solutions (XOR bits?), but this one has interesting usage of try and except

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sing_dict = dict()
        
        for num in nums:
            try:
                sing_dict.pop(num)
            except:
                sing_dict[num] = 0
                
        return sing_dict.keys()[0]