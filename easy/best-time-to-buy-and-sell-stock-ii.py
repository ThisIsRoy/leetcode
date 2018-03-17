# Uses math to solve the problem

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for idx, price in enumerate(prices[:-1]):
            if prices[idx + 1] > prices[idx]:
                profit += prices[idx + 1] - prices[idx]
                
        return profit