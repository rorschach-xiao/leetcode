from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start_pos = 0
        acc_gas, total_acc_gas,start_pos = 0,0,0
        for i in range(n):
            acc_gas += gas[i] - cost[i]
            total_acc_gas += gas[i] - cost[i]
            if acc_gas < 0:
                start_pos = i + 1
                acc_gas = 0
        return -1 if total_acc_gas < 0 else start_pos