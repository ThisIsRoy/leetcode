# Runtime can be improved

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        
        for num in range(N + 1):
            if self.valid_rotate(num):
                count += 1
                
        return count 
        
        
    def valid_rotate(self, n):
        """
        Checks if n is valid after rotating each digit
        """
        inval_set = set(['3', '4', '7'])
        changed_set = set(['2', '5', '6', '9'])
        changed = False
        
        for char in str(n):
            if char in inval_set:
                return False
            
            elif not changed and char in changed_set:
                changed = True
            
        return True if changed else False