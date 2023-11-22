from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            temp = digits[i]
            digits[i] = (digits[i] + carry) % 10
            carry = (temp + carry) // 10
            if carry == 0:
                break
        if carry:
            digits.insert(0, carry)
        return digits