class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = x
        if x < 0:
            return False
        reversed_num = 0
        while origin > 0:
            reversed_num = reversed_num * 10 + origin % 10
            origin //= 10

        return reversed_num == x

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(12112))