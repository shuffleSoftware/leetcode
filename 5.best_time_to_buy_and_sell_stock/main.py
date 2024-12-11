class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') 
        max_profit = 0
        for price in prices:
            if price < min_price: # 1 < 7
                min_price = price # 1
            profit = price - min_price # 
            if profit > max_profit: # 
                max_profit = profit # 6
        return max_profit

# 7
