class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Create a sliding window beginning on right side
        L = len(prices) - 1
        R = len(prices)
        biggest_price = 0
        best_profit = 0
        
        # Loop through array
        while (L > -1):
            print('entered')
            # By going into the array, we are automatically guaranteed at
            # least two values in list

            # Calculate profit at that point
            current_price = prices[L]
            profit = biggest_price - current_price

            best_profit = max(best_profit, profit)
            biggest_price = max(biggest_price, current_price)

            L -= 1



        return best_profit
        