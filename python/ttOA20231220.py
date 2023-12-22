
def getMinCost(cost, compatible1, compatible2, min_compatible):
    if sum(compatible1) < min_compatible or sum(compatible2) < min_compatible:
        return -1
    data = [(c, c1, c2) for c, c1, c2 in zip(cost, compatible1, compatible2)]
    data = sorted(data, key=lambda x: x[0])
    n = len(data)
    min_cost = float('inf')
    def dfs(i, curC1, curC2, cur_cost):
        nonlocal min_cost
        if curC1 >= min_compatible and curC2 >= min_compatible:
            min_cost = min(min_cost, cur_cost)
            return
        for j in range(i, n):
            if data[j][1] == 1:
                curC1 += 1
            if data[j][2] == 1:
                curC2 += 1
            cur_cost += data[j][0]
            dfs(j + 1, curC1, curC2, cur_cost)
            cur_cost -= data[j][0]
            if data[j][1] == 1:
                curC1 -= 1
            if data[j][2] == 1:
                curC2 -= 1
    dfs(0, 0, 0, 0)
    if min_cost == float('inf'):
        return -1
    return min_cost


if __name__ == '__main__':
    cost = [5, 6, 7, 8, 9]
    compatible1 = [1, 1, 0, 0, 1]
    compatible2 = [0, 0, 1, 1, 1]
    min_compatible = 2
    print(getMinCost(cost, compatible1, compatible2, min_compatible))
