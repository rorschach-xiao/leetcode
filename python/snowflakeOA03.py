def findMaxLength(skills, k):
    n = len(skills)
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(k + 1):
            if i == 1:
                dp[i][j] = 1
            else:
                for p in range(1, i):
                    if skills[p - 1] == skills[i - 1]:
                        dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                    elif j != 0:
                        dp[i][j] = max(dp[i][j], dp[p][j - 1] + 1)
                    else:
                        dp[i][j] = max(dp[i][j], dp[p][j])
    return dp[n][k]


if __name__ == '__main__':
    skills = [1, 1, 2, 3]
    k = 0
    print(findMaxLength(skills, k))
