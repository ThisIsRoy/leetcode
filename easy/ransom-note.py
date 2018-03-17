from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = defaultdict(int)
        
        for char in magazine:
            mag_dict[char] += 1
            
        for char in ransomNote:
            if not mag_dict[char]:
                return False
            else:
                mag_dict[char] -= 1
            
        return True