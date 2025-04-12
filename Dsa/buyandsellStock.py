# Buy and sell stock 
# time complexity  = O(n)
# space complexity = O(1)
def findMaxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    
    return max_profit



# Driver code
prices = [7, 1, 5, 3, 6, 4]
maxProfit = findMaxProfit(prices)
print("Maximum profit of buy and sell of stock is:", maxProfit)