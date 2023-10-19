class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while(left < right):
            if self.isAlphanumeric(s[left]) and self.isAlphanumeric(s[right]):
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            if not self.isAlphanumeric(s[left]):
                left += 1
            if not self.isAlphanumeric(s[right]):
                right -= 1
        return True

    def isAlphanumeric(self, c: chr) -> bool:
        if ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
            return True
        return False