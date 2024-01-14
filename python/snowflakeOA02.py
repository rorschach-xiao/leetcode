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
        elif arr[i] == 0 and i < MAX:
            arr[i] = i + 1
            arr[pos_dict[i + 1]] = 0
            ans += 1
        else:
            loop_set = set()
            cur = arr[i]
            while cur != 0 and cur not in loop_set:
                loop_set.add(cur)
                cur = arr[cur - 1]
            if len(loop_set) == 1:
                ans += 1
                ele = loop_set.pop()
                arr[pos_dict[ele]] = 0
                arr[ele - 1] = ele
            else:
                ans += len(loop_set) + 1
                for ele in loop_set:
                    arr[ele - 1] = ele

    return ans


if __name__ == '__main__':
    arr = [3, 2, 1, 0, 0]
    print(getMinSwap(arr))

