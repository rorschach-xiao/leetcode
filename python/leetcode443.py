from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        def rev(i, j):
            while i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1

        n = len(chars)
        if n == 1:
            return 1
        left, write, read = 0, 0, 0
        while read < n:
            if read == n - 1 or chars[read] != chars[read + 1]:
                num = read - left + 1
                chars[write] = chars[read]
                start = write
                write += 1
                if num != 1:
                    while num > 0:
                        chars[write] = str(num % 10)
                        write += 1
                        num //= 10
                    rev(start + 1, write - 1)
                left = read + 1
            read += 1

        return write

if __name__ == '__main__':
    solution = Solution()
    chars = ["a", "b", "b", "b"]
    solution.compress(["a", "b", "b", "b"])
    print(chars)