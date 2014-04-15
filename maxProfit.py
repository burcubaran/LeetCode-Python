class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices==[]:
            return 0
        profit=0
        pmin=prices[0]
        for i in range(len(prices)):
            if prices[i]<pmin:
                pmin=prices[i]
            else:
                profit=max(prices[i]-pmin, profit)
        return profit
