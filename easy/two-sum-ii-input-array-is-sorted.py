# Beat 97%!

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = len(numbers) - 1
        add = numbers[index1] + numbers[index2]
        while add != target:
            if add > target:
                index2 -= 1
            
            else:
                index1 += 1
            
            add =  numbers[index1] + numbers[index2]
        
        return [index1 + 1, index2 + 1]