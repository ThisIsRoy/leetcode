# O(n) solution using defaultdict

from collections import defaultdict

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter_dict = defaultdict(int)
        
        for char in s:
            letter_dict[char] += 1 
        
        t_dict = defaultdict(int)
        for char in t:
            
            # found letter that didn't appear
            if not letter_dict[char]:
                return char
            
            else: 
                t_dict[char] += 1
        
        # check which letter appeared 
        for char in t_dict:
            if t_dict[char] != letter_dict[char]:
                return char
                