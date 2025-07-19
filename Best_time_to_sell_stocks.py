class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profi = 0
        for i in range(1, len( prices)):
            
            if prices[i] < mini :
                mini = prices[i]

            elif prices[i] - mini > profi:
                profi = prices[i] - mini

        return profi
