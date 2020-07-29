'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''
#Solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for i in range(n+1)]
        dp[1][1] = 0 - prices[0] 
        for i in range(2, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])    #don't buy or sell
            dp[i][1] = max(dp[i-2][0] - prices[i-1], dp[i-1][1])     # buy on i-th day or don't buy
        return max(dp[-1])
        
        
        
