class Solution:
    def addBinary(self, a: str, b: str) -> str:
        re = []
        p1, p2 = len(a) - 1, len(b) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0:
            if p1 >= 0:
                carry += int(a[p1])
                p1 -= 1

            if p2 >= 0:
                carry += int(b[p2])
                p2 -= 1
            re.insert(0, str(carry % 2))
            carry //= 2

        if carry != 0:
            re.insert(0, "1")

        return "".join(re)