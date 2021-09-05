"""
圆环上有10个点，编号为0~9。从0点出发，每次可以逆时针和顺时针走一步，问走n步回到0点共有多少种走法。
input: 2
output: 2
0->1->0 ; 0->9->0
"""
class Solution():
    def backToOrigin(self,n):
        length=10
        dp = [[0 for _ in range(length)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(length):
                dp[i][j] = dp[i-1][(j-1+length)%length] +dp[i-1][(j+1)%length]
        return dp[n][0]

if __name__ == '__main__':
    solution = Solution()
    print(solution.backToOrigin(2))
