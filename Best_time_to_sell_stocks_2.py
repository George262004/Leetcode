class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profi=0

        for i in range(1,len(prices)):
            if prices[i] > prices[i -1]:
                profi += prices[i] - prices[i-1]
    

        return profi
            
