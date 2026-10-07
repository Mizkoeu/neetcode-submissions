class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(0, prices[i]-prices[i-1])
        return max_profit