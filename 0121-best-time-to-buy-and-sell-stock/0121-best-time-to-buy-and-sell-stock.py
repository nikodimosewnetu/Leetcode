class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        profit=0
        for price in prices:
            if price<min_price:
                min_price=price
        
            p=price-min_price
            profit=max(profit,p)
              

        return profit
            
      
            