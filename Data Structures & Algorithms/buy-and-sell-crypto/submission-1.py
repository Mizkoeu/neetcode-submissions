class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                max_profit = max(max_profit, price - min_so_far)

        return max_profit