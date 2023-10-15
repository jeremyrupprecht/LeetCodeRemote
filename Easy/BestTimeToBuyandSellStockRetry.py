# 121 Best Time to Buy and Sell Stock Redo
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

def maxProfit(prices):
    profit = 0
    l = 0
    for r in range(len(prices)):
        if prices[r] < prices[l]:
            l = r
            r = l + 1
        if r != len(prices) and prices[r] - prices[l] > profit:
            profit = prices[r] - prices[l]
    return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    prices2 = []
    prices3 = [1,2,3,4]
    prices4 = [4,3,2,1]
    print(maxProfit(prices4))
