import copy


def countMinimumCharacters(s, arr):
    def comp(a, b):
        for p in range(10):
            if a[p] > b[p]:
                return 0
        return 1
    def count(s):
        cnt = []
        for i in range(10):
            cnt.append(s.count(str(i)))
        return cnt
    ans = []
    n = len(s)
    total_cnt = [[0 for _ in range(10)] for _ in range(n + 1)]
    for i, c in enumerate(s):
        total_cnt[i + 1] = copy.copy(total_cnt[i])
        total_cnt[i + 1][ord(c) - ord('0')] += 1

    for tar_s in arr:
        cnt_dict = count(tar_s)
        # binary search
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if comp(cnt_dict, total_cnt[mid]) > 0:
                right = mid
            else:
                left = mid + 1
        if comp(cnt_dict, total_cnt[left]) == 0:
            ans.append(-1)
        else:
            ans.append(left)
    return ans

if __name__ == '__main__':
    s = "111222333444"
    arrs = ["121", "3", "12345", "11234"]
    print(countMinimumCharacters(s, arrs))