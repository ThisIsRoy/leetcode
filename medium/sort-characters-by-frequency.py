# Beats 94%!

from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
            
        freq_list = []
        for char, num in char_dict.items():
            freq_list.append((char, num))
            
        freq_list.sort(key = lambda x: x[1], reverse = True)
        
        sorted_str = ''
        for item in freq_list:
            sorted_str += item[0] * item[1]
            
        return sorted_str