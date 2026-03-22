def max_profit(prices):
    """
    # Find the maximum profit from buying and selling a stock once.
    # You must buy before you sell.
    """
    if len(prices) < 2: return 0

    best = 0 
    min_price = prices[0] 
    for i in range(len(prices)):
        profit = prices[i] - min_price
        if profit > best:
            best = profit
        
        if prices[i] < min_price:
            min_price = prices[i]
    return best

    # # 3. Outer loop: Pick a day to buy
    # for i in range(len(prices)):
    #     buy = prices[i]
        
    #     # 4. Inner loop: Pick a day to sell (must be AFTER the buy day)
    #     for j in range(i + 1, len(prices)):
    #         sell = prices[j]
            
    #         # 5. Calculate profit and update if it's the best we've seen
    #         if sell - buy > best:
    #             best = sell - buy


# --- Runnable Example ---
print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected: 5 (buy at 1, sell at 6)
print(max_profit([7, 6, 4, 3, 1]))      # Expected: 0 (no profit possible)

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - We loop through the prices list only once.
    
    * Space Complexity: O(1)
      - We only use two variables: min_price and best.
"""


