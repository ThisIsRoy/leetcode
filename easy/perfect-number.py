import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        
        max_iter = int(math.ceil(math.sqrt(num)))
        
        divisors = set([1])
        for divid in range(2, max_iter):
            if num % divid == 0:
                divisors.add(divid)
                divisors.add(num / divid)
                
        return True if sum(divisors) == num else False
        