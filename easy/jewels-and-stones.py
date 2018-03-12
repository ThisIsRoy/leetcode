from collections import defaultdict

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_dict = defaultdict(lambda: False)
        jewel_count = 0
        
        for jewel in J:
            jewel_dict[jewel] = True
            
        for stone in S:
            if jewel_dict[stone]:
                jewel_count += 1
            
        return jewel_count 