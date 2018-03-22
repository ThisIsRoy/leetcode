# originally used stack, but was too slow because of array manipulation
# revised solution simply uses pointer

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        idx = 0
        assigned = 0
        cookies = len(s)
        
        for child in g:
            while idx < cookies:
                if s[idx] >= child:
                    assigned += 1
                    idx += 1
                    break
                    
                idx += 1
        return assigned