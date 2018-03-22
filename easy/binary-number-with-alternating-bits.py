# Oops, realized there is a built-in function to conver to binary 

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_str = self.num_to_bin(n)
        for char_idx in range(1, len(bin_str)):
            if bin_str[char_idx - 1] == bin_str[char_idx]:
                return False
            
        return True
    
    def num_to_bin(self, num):
        if num <= 1:
            return str(num)
        else:
            return self.num_to_bin(num / 2) + self.num_to_bin(num % 2)