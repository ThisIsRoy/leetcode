# second solution is an improved version of first, speeds up significant when using if instead of max(), why?

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # solution 1
#         if prices == []:
#             return 0
        
#         buy = prices[0]
#         sell = prices[0]
#         maybe = None
        
#         for price in prices[1:]:
#             if maybe >= 0 and price < maybe:
#                 maybe = price
            
#             elif maybe >= 0 and price - maybe > sell - buy:
#                 buy = maybe
#                 sell = price
#                 maybe = None
            
#             elif price > sell:
#                 sell = price
                
#             elif maybe == None and price < buy:
#                 maybe = price
                
#         return sell - buy

        # solution 2
    
        if prices == []:
            return 0
        
        buy = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < buy:
                buy = price
            # originally used profit = max(profit, price - buy), very slow 
            elif price - buy > profit:
                profit = price - buy
                
        return profit