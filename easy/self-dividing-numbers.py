class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_div = list()
        for num in range(left, right + 1):
            if self.is_self_divide(num):
                self_div.append(num)
        
        return self_div
        
    def is_self_divide(self, num):
        for str_digit in str(num):
            
            if str_digit == '0' or num % int(str_digit) != 0:
                return False
            
        return True