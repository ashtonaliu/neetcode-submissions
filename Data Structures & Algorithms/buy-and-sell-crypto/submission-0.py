class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        sell = prices[len(prices) - 1]
        max_profit = 0
        for i in range(len(prices) - 2, -1, -1):
            buy = prices[i]
            max_profit = max(max_profit, sell - buy)
            sell = max(sell, buy)
        return max_profit