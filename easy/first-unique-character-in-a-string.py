from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
            
        for idx, char in enumerate(s):
            if char_dict[char] == 1:
                return idx
            
        return -1