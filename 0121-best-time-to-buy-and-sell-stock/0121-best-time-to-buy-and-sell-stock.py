class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minP = float('inf')
        for i in range(len(prices)):
            minP = min(minP, prices[i])
            maxPro = max(maxPro, prices[i] - minP)
        return maxPro
#         BRUTE 
        # maxP = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if prices[j]>prices[i]:
        #             maxP = max(prices[j] - prices[i], maxP)
        # return maxP
                    
        
        
        