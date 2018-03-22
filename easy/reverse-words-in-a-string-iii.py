class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        reversed_s = words[0][::-1]
        for word in words[1:]:
            reversed_s += ' '
            reversed_s += word[::-1]
            
        return reversed_s