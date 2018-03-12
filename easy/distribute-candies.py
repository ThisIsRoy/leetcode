class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        unique_candy = set()
        for candy in candies:
            unique_candy.add(candy)
            
        return min(len(candies)/2, len(unique_candy))