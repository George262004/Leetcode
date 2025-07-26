class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        cur_gas = 0
        total_gas = 0

        for i in range(len(gas)):
            fuel_gain = gas[i] - cost[i]
            cur_gas += fuel_gain
            total_gas += fuel_gain

            if cur_gas < 0:
                cur_gas = 0
                start = i + 1

        return -1 if total_gas < 0 else start
