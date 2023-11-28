class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        p1, p2 = 0, 0
        n1, n2 = len(str1), len(str2)
        lenOfGcd = self.gcd(n1, n2)
        t1 = n1 // lenOfGcd
        t2 = n2 // lenOfGcd
        if str1[:lenOfGcd] == str2[:lenOfGcd] and str1[:lenOfGcd] * t1 == str1 and str2[:lenOfGcd] * t2 == str2:
            res = str1[:lenOfGcd]
        return res

    def gcd(self, a, b):
        reminder = a % b
        while reminder != 0:
            a = b
            b = reminder
            reminder = a % b
        return b