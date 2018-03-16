# O(1) requires knowledge of digit root
# Formula is 1 + (num - 1) % 9

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """    
        while len(str(num)) > 1:
            dig_list = []
            for char in str(num):
                dig_list.append(int(char))
                
            num = sum(dig_list)
            
        return num 