class Solution:
    def intToRoman(self, num: int) -> str:
        int2romanDict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        re = ""
        intNumsList = sorted(int2romanDict.keys(), reverse=True)
        n = len(intNumsList)
        for i in range(n):
            if num // intNumsList[i] != 0:
                re += int2romanDict[intNumsList[i]] * (num // intNumsList[i])
                num = num % intNumsList[i]

        return re

if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(1994))