# Interesting behavior from defaultdict and keys when accessed

from collections import defaultdict

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # Create a dictionary of the character orders given by S
        order_dict = defaultdict(lambda: False)
        idx = 1
        for char in S:
            order_dict[char] = idx
            idx += 1
        
        # Create a dictionary of the number of occurances of each char in T
        extra = ''
        str_count = defaultdict(int)
        for char in T:
            if order_dict[char]:
                str_count[char] += 1
                
            else:
                extra += char
        
        str_list = ['' for _ in range(len(order_dict.keys()))]
        
        for char, order in order_dict.items():
            str_list[order - 1] = char * str_count[char]
            
        return ''.join(str_list) + extra
            