def getMinSwap(arr):
    n = len(arr)
    MAX = max(arr)
    ans = 0
    pos_dict = {}
    for i in range(n):
        if arr[i] != 0:
            pos_dict[arr[i]] = i

    for i in range(n):
        if arr[i] == i + 1 or (arr[i] == 0 and i >= MAX):
            continue
        else:
            loop_set = set()
            cur = arr[i]
            while cur != 0 and cur not in loop_set:
                loop_set.add(cur)
                cur = arr[cur - 1]
            if cur == 0:
                ans += len(loop_set)
                for ele in loop_set:
                    arr[ele - 1] = ele
                arr[i] = 0
                arr[i], arr[pos_dict[i + 1]] = arr[pos_dict[i + 1]], arr[i]
                ans += 1
            else:
                ans += len(loop_set) + 1
                for ele in loop_set:
                    arr[ele - 1] = ele
    return ans


if __name__ == '__main__':
    arr = [1, 0, 0, 3, 2]
    print(getMinSwap(arr))
