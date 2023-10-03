# 121 Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    bDay = 0
    sDay = 1
    finalProfit = 0
    while sDay <= len(prices) - 1:
        if prices[bDay] < prices[sDay]:
            profit = prices[sDay] - prices[bDay]
            finalProfit = max(finalProfit, profit)
            sDay += 1
        else:
            bDay = sDay
            sDay = bDay + 1
    return finalProfit

if __name__ == "__main__":

    prices = [7,1,5,3,6,4]      # length = 6
    prices2 = [7,1,5]
    prices3 = [6,5,4,3,2,1]
    prices4 = [1]
    print(maxProfit(prices2))