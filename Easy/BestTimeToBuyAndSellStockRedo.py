# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    maxProfit = 0
    buyDay = 0
    sellDay = 1
    while sellDay < len(prices):
        if (prices[buyDay] <= prices[sellDay]):
            currentProfit = prices[sellDay] - prices[buyDay]
            maxProfit = max(maxProfit, currentProfit)
            sellDay += 1
        else:
            buyDay = sellDay
            sellDay += 1
    return maxProfit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    prices2 = [7,6,4,3,1]
    prices3 = [1,2]
    print(maxProfit(prices2))
