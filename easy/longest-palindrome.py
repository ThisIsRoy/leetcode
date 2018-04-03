from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        let_dict = defaultdict(int)
        count = 0 
        
        for char in s:
            if let_dict[char]:
                let_dict.pop(char)
                count += 1
                
            else:
                let_dict[char] += 1
                
        if count * 2 == len(s):
            return count * 2
        else:
            return count * 2 + 1
        