from collections import defaultdict

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        char_dict = defaultdict(int)
        min_idx = float('inf')
        min_list = []
        
        for idx in range(len(list1)):
            char_dict[list1[idx]] = idx + 1
        
        for idx in range(len(list2)):
            curr_val = char_dict[list2[idx]]
            if curr_val:
                if idx + curr_val < min_idx:
                    min_idx = idx + curr_val
                    min_list = [list2[idx]]
                
                elif idx + curr_val == min_idx:
                    min_list.append(list2[idx])
                    
        return min_list
        